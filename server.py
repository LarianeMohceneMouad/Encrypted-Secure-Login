import sqlite3
import hashlib
import socket
import threading
import rsa

public_key, private_key = rsa.newkeys(1024)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()


def handle_connection(c):
    c.send(public_key.save_pkcs1('PEM'))
    pkey_client = rsa.PublicKey.load_pkcs1(client.recv(1024))
    c.send(rsa.encrypt("username: ".encode(), pkey_client))
    username = rsa.decrypt(c.recv(1024), private_key).decode()
    c.send(rsa.encrypt("password: ".encode(), pkey_client))
    password = rsa.decrypt(c.recv(1024), private_key)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM userdata WHERE username = ? and password = ?", (username, password))

    if cursor.fetchall():
        c.send(rsa.encrypt("Login Successful".encode(), pkey_client))
    else:
        c.send(rsa.encrypt("Login Failed".encode(), pkey_client))


while True:
    client, _ = server.accept()
    threading.Thread(target=handle_connection, args=(client, )).start()


