from collections import deque

class DequeDemo:
    def demo(self):
        dq = deque(["API", "Database", "UI"])
        dq.append("Security")
        dq.appendleft("Performance")
        print("Queue after adding:", dq)
        dq.pop()
        dq.popleft()
        print("Queue after removing:", dq)
