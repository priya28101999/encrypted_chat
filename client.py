import socket
from cryptography.fernet import Fernet

# Paste the key you copied from server here
key = b'PASTE_YOUR_SERVER_KEY_HERE'
cipher = Fernet(key)

# Connect to server
client = socket.socket()
client.connect(("127.0.0.1", 5555))
print("Connected to server")

while True:
    # Type a message to send
    msg = input("You: ")
    encrypted = cipher.encrypt(msg.encode())
    client.send(encrypted)

    # Receive reply from server
    reply = cipher.decrypt(client.recv(1024)).decode()
    print("Server:", reply)
