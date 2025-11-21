# Decorator with arguments example

def decorator_with_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper


@decorator_with_arguments
def add(a, b):
    return a + b


if __name__ == "__main__":
    add(10, 20)
