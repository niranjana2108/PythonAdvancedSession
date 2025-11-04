# main.py
"""
Day 02 - Yield Statement & Iteration Protocols
Topics:
• yield and yield from
• Infinite generators
• send() and generator pipelines
• Iteration protocol behind loops
"""

from yield_examples import yield_from_example,simple_generator
from infinite_generators import infinite_counter
from send_example import echo_generator
from generator_pipelines import numbers, square, cube

def demo_iteration_protocol():
    print("\n=== Iteration Protocol Demo ===")
    nums = [10, 20, 30]
    iterator = iter(nums)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of iteration.")
            break

if __name__ == "__main__":
    print("=== DAY 02: Generators & Iteration Protocols ===")

    print("=== Simple Generator Example ===")
    for val in simple_generator():
        print(val)
    yield_from_example()
    demo_iteration_protocol()

    # Infinite generator (limited loop for safety)
    print("\n=== Infinite Generator Example ===")
    gen = infinite_counter()
    for i in range(5):
        print(next(gen))

    # send() example
    print("\n=== send() Example ===")
    gen = echo_generator()
    next(gen)
    gen.send("Python")
    gen.send("Rocks!")

    # Pipeline example
    print("\n=== Generator Pipeline ===")
    for val in cube(square(numbers())):
        print(val)
