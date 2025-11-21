# Context Manager using a Class

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_type}")
        return True  # suppresses exceptions


if __name__ == "__main__":
    with FileManager("demo.txt", "w") as f:
        f.write("Hello from context manager!")
