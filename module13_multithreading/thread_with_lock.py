# module11_multithreading/thread_with_lock.py
import threading

counter = 0
lock = threading.Lock()


def increment():
    global counter
    for _ in range(100000):
        with lock:  # critical section
            counter += 1


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
