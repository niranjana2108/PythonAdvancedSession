# module1_generators_iterators/generator_examples.py

def count_upto_five():
    n = 1
    while n <= 5:
        yield n
        n += 1


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        # a, b = b, a + b
        a=b
        b=a+b

def run_generators():
    print("\n=== Simple Generator Example ===")
    for num in count_upto_five():
        print(num)

    print("\n=== Fibonacci Generator Example ===")
    for num in fibonacci(10):
        print(num)
