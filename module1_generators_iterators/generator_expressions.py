# module1_generators_iterators/generator_expressions.py

def run_generator_expression():
    print("\n=== Generator Expression Example ===")

    squares_list = [x * x for x in range(5)]
    print("List comprehension:", squares_list)

    squares_gen = (x * x for x in range(5))
    print("Generator object:", squares_gen)

    print("Values from generator:")
    for s in squares_gen:
        print(s)
