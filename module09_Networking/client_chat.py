import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 5001))

    print("Connected to server! Type your message.")
    print("Type 'exit' to end the chat.\n")

    while True:
        # send message
        msg = input("You (Client): ")
        client.send(msg.encode())

        if msg.lower() == "exit":
            print("Client ended the chat.")
            break

        # receive reply
        reply = client.recv(1024).decode()
        if reply.lower() == "exit":
            print("Server ended the chat.")
            break

        print("Server:", reply)

    client.close()


if __name__ == "__main__":
    start_client()
