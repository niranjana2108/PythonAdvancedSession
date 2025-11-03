# send_example.py

def echo_generator():
    received = None
    while True:
        received = yield f"Received: {received}"
        print(f"Echoed value: {received}")

if __name__ == "__main__":
    print("=== send() Example ===")
    gen = echo_generator()
    print(next(gen))      # Start the generator
    print(gen.send("Hello"))
    print(gen.send("World"))
    gen.close()
