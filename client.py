import socket
import rsa

public_key, private_key = rsa.newkeys(1024)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))

pkey_server = rsa.PublicKey.load_pkcs1(client.recv(1024))
client.send(public_key.save_pkcs1('PEM'))
# c.send(rsa.encrypt("username: ".encode(), pkey_client))
message = rsa.decrypt(client.recv(1024), private_key).decode()
client.send(rsa.encrypt(input(message).encode(), pkey_server))
message = rsa.decrypt(client.recv(1024), private_key).decode()
client.send(rsa.encrypt(input(message).encode(), pkey_server))
print(rsa.decrypt(client.recv(1024), private_key).decode())
