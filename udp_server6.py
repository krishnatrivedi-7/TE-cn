import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 12345))
print("Server ready... waiting for file")

fname, addr = s.recvfrom(1024)
fname = fname.decode()
print(f"Receiving file: {fname}")

with open("received_" + fname, 'wb') as f:
    while True:
        data, _ = s.recvfrom(1024)
        if data == b'EOF':
            break
        f.write(data)

print(f"File '{fname}' received successfully.")
s.close()
