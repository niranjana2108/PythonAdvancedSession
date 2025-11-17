import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5001))
    server.listen(1)

    print("Server waiting for client to connect...")
    conn, addr = server.accept()
    print(f"Client connected from: {addr}")

    while True:
        # receive message
        client_msg = conn.recv(1024).decode()
        if client_msg.lower() == "exit":
            print("Client ended the chat.")
            break

        print("Client:", client_msg)

        # send reply
        server_msg = input("You (Server): ")
        conn.send(server_msg.encode())

        if server_msg.lower() == "exit":
            print("Server ended the chat.")
            break

    conn.close()
    server.close()


if __name__ == "__main__":
    start_server()
