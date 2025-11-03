# infinite_generators.py
import time

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

if __name__ == "__main__":
    print("=== Infinite Counter ===")
    counter = infinite_counter()
    for num in counter:
        print(num)
        time.sleep(0.5)
        if num == 5:
            print("Breaking loop...")
            break
