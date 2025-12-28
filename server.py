import socket
from cryptography.fernet import Fernet

# Generate key (or use a pre-shared key)
key = Fernet.generate_key()
cipher = Fernet(key)

# Setup server
server = socket.socket()
server.bind(("127.0.0.1", 5555))
server.listen(1)

print("Encryption Key (COPY THIS for client):", key)
print("Server listening on port 5555...")

conn, addr = server.accept()
print("Client connected:", addr)

while True:
    # Receive message from client
    data = conn.recv(1024)
    if not data:
        break
    message = cipher.decrypt(data).decode()
    print("Client:", message)

    # Type reply and send to client
    reply = input("You: ")
    encrypted_reply = cipher.encrypt(reply.encode())
    conn.send(encrypted_reply)

conn.close()
