# module11_multithreading/thread_with_class.py
import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(3):
            print(f"[{self.name}] Working on task {i}")
            time.sleep(1)


def main():
    t1 = WorkerThread("Worker-1")
    t2 = WorkerThread("Worker-2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All worker threads completed.")


if __name__ == "__main__":
    main()
