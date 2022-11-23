# Encrypted-Secure-Login
Secure login system in python using RSA Encrypted communication and password hashing

## Installing necessary libraries:
``pip install -r requirements.txt``

### 1. Creating userdata samples : ** using SQLite3 in python
Storing passwords hashes in our usedata database

### 2. RSA Encrypted Communication : 
Both server and client exchange RSA public keys at the beginning of the session, than all messages are Encrypted with the public key of the received, and then Decrypted when received with the receiver's private key.

### 3. Checking passwords : 
The server hashes the password and compare it with the hash in the database, if they are equal than the client logs in successfully, else the client won't be able to log in (login failed)
