#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = len(sys.argv) - 1
    args = sys.argv

    if argv < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(args[1])
    b = int(args[3])
    operator = args[2]

    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
