# module11_multithreading/thread_safe_queue.py
import time
import threading
from queue import Queue


queue = Queue()


def producer():
    for i in range(5):
        print(f"[Producer] Producing item {i}")
        queue.put(i)
        time.sleep(1)
    queue.put(None)  # sentinel value for stopping consumer


def consumer():
    while True:
        item = queue.get()
        if item is None:
            print("[Consumer] No more items. Exiting...")
            break

        print(f"[Consumer] Consumed item {item}")
        time.sleep(2)


def main():
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Producer and Consumer finished.")


if __name__ == "__main__":
    main()
