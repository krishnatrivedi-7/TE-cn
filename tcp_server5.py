import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server ready... waiting for connection")
conn, addr = s.accept()
print("Connected to:", addr)

# a. Say hello to each other
msg = conn.recv(1024).decode()
print("Client:", msg)
conn.send(b"Hello from Server")

# b. File transfer
fname = conn.recv(1024).decode()
with open(fname, 'wb') as f:
    data = conn.recv(1024)
    while data:
        f.write(data)
        data = conn.recv(1024)
print(f"File '{fname}' received successfully.")
conn.close()
