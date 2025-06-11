import argparse

def main():
    parser = argparse.ArgumentParser(description="simpel comandline calculator")

    parser.add_argument(
        "num1", type=float, help="first number"
    )
    parser.add_argument(
        "num2", type=float,help="second number"
    )
    parser.add_argument(
        "operation", choices=["add", "subtract","multiply"], help="performs addition, subtraction, or multiplication"
    )

    args = parser.parse_args()

    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "subtract":
        result = args.num1 - args.num2
    elif args.operation == "multiply":
        result = args.num1 * args.num2
    else:
        print("invalid operation")
        return
    
    print(f"Result: {result}")


if __name__ =="__main__":
    main()