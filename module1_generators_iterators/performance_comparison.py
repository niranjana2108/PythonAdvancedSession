# module1_generators_iterators/performance_comparison.py

import sys

def compare_list_vs_generator():
    print("\n=== Performance Comparison ==")

    nums_list = [x for x in range(1000000)]
    nums_gen = (x for x in range(1000000))

    print("List size in bytes:", sys.getsizeof(nums_list))
    print("Generator size in bytes:", sys.getsizeof(nums_gen))
