import argparse
from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


@log_function_call
def add(x, y):
    return x + y

@log_function_call
def subtract(x, y):
    return x - y

@log_function_call
def multiply(x, y):
    return x * y


def main():
    parser = argparse.ArgumentParser(description="Command-line calculator with logging.")
    parser.add_argument("num1", type=float, help="First number.")
    parser.add_argument("num2", type=float, help="Second number.")
    parser.add_argument("operation", choices=["add", "subtract", "multiply"],
                        help="Arithmetic operation to perform.")

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "subtract":
        result = subtract(args.num1, args.num2)
    elif args.operation == "multiply":
        result = multiply(args.num1, args.num2)

    print(f"Final Result: {result}")

if __name__ == "__main__":
    main()