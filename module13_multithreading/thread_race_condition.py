# module11_multithreading/thread_race_condition.py
import threading
import time

counter = 0  # shared resource


def increment():
    global counter
    for _ in range(100000):
        counter += 1  # race condition happens here


def main():
    global counter
    counter = 0

    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Expected value 200000")
    print("Actual value:", counter)


if __name__ == "__main__":
    main()
