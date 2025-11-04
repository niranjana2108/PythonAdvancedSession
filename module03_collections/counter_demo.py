from collections import Counter

class CounterDemo:
    def demo(self):
        words = ["api", "api", "test", "automation", "test", "framework", "test"]
        word_count = Counter(words)
        print("Word Frequency:", word_count)
        print("Most common:", word_count.most_common(2))
