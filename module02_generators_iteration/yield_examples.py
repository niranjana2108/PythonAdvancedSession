# yield_examples.py

def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"

def yield_from_example():
    def sub_generator():
        yield 1
        yield 2
        yield 3

    def main_generator():
        yield "Start"
        yield from sub_generator()
        yield "End"

    for item in main_generator():
        print(item)


if __name__ == "__main__":
    print("=== Simple Generator Example ===")
    for val in simple_generator():
        print(val)

    print("\n=== yield from Example ===")
    yield_from_example()
