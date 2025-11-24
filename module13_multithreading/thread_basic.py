# module11_multithreading/thread_basic.py
import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"[Thread] Number: {i}")
        time.sleep(0.5)


def main():
    print("Main thread starting...")

    t1 = threading.Thread(target=print_numbers)
    t1.start()
    t1.join()  # wait for thread to finish

    print("Main thread finished.")


if __name__ == "__main__":
    main()
