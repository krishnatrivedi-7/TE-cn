import socket, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('localhost', 12345)

fname = input("Enter file name to send: ")

if os.path.exists(fname):
    s.sendto(fname.encode(), server)
    with open(fname, 'rb') as f:
        data = f.read(1024)
        while data:
            s.sendto(data, server)
            data = f.read(1024)
    s.sendto(b'EOF', server)
    print(f"File '{fname}' sent successfully.")
else:
    print("File not found.")
s.close()


# How to Perform in VS Code
# Step 1️⃣ — Create two Python files:

# udp_server.py

# udp_client.py

# Put both in the same folder.

# Step 2️⃣ — Prepare any file to send

# Example files:

# sample.txt      → Text file  
# song.mp3        → Audio file  
# video.mp4       → Video file  
# test.py         → Script file


# (You can test with just sample.txt first.)

# Step 3️⃣ — Open two terminals in VS Code
# Terminal 1 (Server)
# python udp_server.py


# Output:

# Server ready... waiting for file

# Terminal 2 (Client)
# python udp_client.py


# Input:

# Enter file name to send: sample.txt

# 🖥️ Example Output

# Client side:

# Enter file name to send: sample.txt
# File 'sample.txt' sent successfully.


# Server side:

# Server ready... waiting for file
# Receiving file: sample.txt
# File 'sample.txt' received successfully.


# The received file will be saved as
# 📄 received_sample.txt

# ✅ Viva Explanation (Simple)

# UDP (User Datagram Protocol) is connectionless (no handshake).

# Here, we use socket.SOCK_DGRAM.

# Server listens on a port and receives file data packets.

# Client sends file chunks and ends with "EOF".

# Works for any file type — text, audio, video, or script.