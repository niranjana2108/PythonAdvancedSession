# generator_pipelines.py

def numbers():
    for i in range(1, 6):
        yield i

def square(nums):
    for n in nums:
        yield n * n

def cube(nums):
    for n in nums:
        yield n * n * n

if __name__ == "__main__":
    print("=== Generator Pipeline ===")
    nums = numbers()
    squared = square(nums)
    cubed = cube(squared)
    for val in cubed:
        print(val)
