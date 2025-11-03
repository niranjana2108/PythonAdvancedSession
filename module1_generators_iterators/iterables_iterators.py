# module1_generators_iterators/iterables_iterators.py

def show_iterable_example():
    print("=== Iterable Example ===")
    numbers = [1, 2, 3]
    for num in numbers:
        print(num)


def show_iterator_example():
    print("\n=== Iterator Example ===")
    numbers = [1, 2, 3]
    it = iter(numbers)
    print(next(it))
    print(next(it))
    a=15
    print(a)
    print(next(it))
    # Uncomment below to see StopIteration error
    # print(next(it))
