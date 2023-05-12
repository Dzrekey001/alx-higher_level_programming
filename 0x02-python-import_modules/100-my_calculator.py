#!/usr/bin/python3
from calculator import add, sub, mul, div
import sys
if __name__ == "__main__":
    arg_len = len(sys.argv) - 1

    if arg_len < 3 or arg_len > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            result = add(a, b)
            print("{} + {} = {}".format(a, b, result))
        elif sys.argv[2] == "-":
            result = sub(a, b)
            print("{} - {} = {}".format(a, b, result))
        elif sys.argv[2] == "*":
            result = mul(a, b)
            print("{} * {} = {}".format(a, b, result))
        elif sys.argv[2] == "/":
            result = div(a, b)
            print("{} / {} = {}".format(a, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
