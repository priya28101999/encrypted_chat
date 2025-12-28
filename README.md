# Encrypted Chat App

This is a simple client-server chat application with **AES/Fernet encryption**.

## Features
- Messages are encrypted before sending
- Uses TCP sockets
- One client at a time
- Server prints client messages and can reply

## How to run
1. Start server:
   python3 server.py
2. Copy the encryption key from server output
3. Paste it in client.py
4. Start client:
   python3 client.py
5. Chat securely!
