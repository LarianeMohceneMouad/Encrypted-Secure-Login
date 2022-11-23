import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "lmouuud", hashlib.sha256("lmouuudpw".encode()).hexdigest()
username2, password2 = "johnwick", hashlib.sha256("johnwickpw".encode()).hexdigest()
username3, password3 = "merry4real", hashlib.sha256("merrypw".encode()).hexdigest()
username4, password4 = "sarah123", hashlib.sha256("sarahpw".encode()).hexdigest()

cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cursor.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()

