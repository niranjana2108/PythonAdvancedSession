# Context Manager using contextlib

from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    print("Opening file...")
    f = open(name, mode)
    try:
        yield f
    finally:
        print("Closing file...")
        f.close()


if __name__ == "__main__":
    with open_file("demo2.txt", "w") as f:
        f.write("Hello using contextlib!")
