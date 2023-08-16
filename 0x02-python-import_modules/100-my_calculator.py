#!/usr/bin/python3
# Import all functions from calculator_1.py
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    # Get the arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    # Check if the operator is valid
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    # Perform the operation
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))
