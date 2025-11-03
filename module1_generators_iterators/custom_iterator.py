# module1_generators_iterators/custom_iterator.py

class CountUptoFive:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration


def run_custom_iterator():
    print("\n=== Custom Iterator Example ===")
    for n in CountUptoFive():
        print(n)
