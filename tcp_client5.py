import socket

c = socket.socket()
c.connect(('localhost', 12345))

# a. Say hello to each other
c.send(b"Hello from Client")
print("Server:", c.recv(1024).decode())

# b. File transfer
fname = input("Enter file name to send: ")
c.send(fname.encode())
with open(fname, 'rb') as f:
    data = f.read(1024)
    while data:
        c.send(data)
        data = f.read(1024)
print("File sent successfully.")
c.close()

# How to Perform in VS Code
# Step 1️⃣ — Create two files:

# tcp_server.py

# tcp_client.py

# Step 2️⃣ — Prepare a file to send

# Make a text file in the same folder, e.g.
# 📄 data.txt containing:

# Hello, this is a test file.

# Step 3️⃣ — Run the programs

# Open two terminals in VS Code:

# In Terminal 1, run:

# python tcp_server.py


# In Terminal 2, run:

# python tcp_client.py

# Step 4️⃣ — Give input in client
# Enter file name to send: data.txt

# Step 5️⃣ — Output you’ll see

# Server side:

# Server ready... waiting for connection
# Connected to: ('127.0.0.1', 56789)
# Client: Hello from Client
# File 'data.txt' received successfully.


# Client side:

# Server: Hello from Server
# Enter file name to send: data.txt
# File sent successfully.