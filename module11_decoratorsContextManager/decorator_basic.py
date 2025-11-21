# Basic Decorator Example

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        print("Wrapper")
        func()
        print("After the function runs")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


if __name__ == "__main__":
    say_hello()
