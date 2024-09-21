import argparse

if __name__ == "__main__":
    # Create an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser()
    # Define a command-line arguments
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation", \
                        choices=["add","subtract","multiply"])

    # Parse the command-line arguments and store them in the 'args' object
    args = parser.parse_args()


    print(args.number1)
    print(args.number2)
    print(args.operation)

    # Convert the string inputs into integers
    n1=int(args.number1)
    n2=int(args.number2)
    result = None
    if args.operation == "add":
        result=n1+n2
    elif args.operation == "subtract":
        result=n1-n2
    elif args.operation == "multiply":
        result=n1*n2


    print("Result:",result)