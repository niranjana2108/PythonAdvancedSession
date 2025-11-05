from collections import deque

class DequeDemo:
    def demo(self):
        dq = deque(["API", "Database", "UI"])
        dq.append("Security")
        dq.appendleft("Performance")
        print("Queue after adding:", dq)
        dq.pop()
        print("Queue after removing:", dq)
        dq.popleft()
        print("Queue after removing:", dq)

if __name__ == "__main__":

    print("\n=== Deque Demo ===")
    DequeDemo().demo()