import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for client...")
conn, addr = server.accept()
print("Connected:", addr)

msg = conn.recv(1024).decode()
print("Client:", msg)

conn.send("Hello from server!".encode())
conn.close()
