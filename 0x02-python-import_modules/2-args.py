#!/usr/bin/python3
import sys
arg_len = len(sys.argv)

if arg_len == 1:
    print("0 arguments.")
elif arg_len == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(arg_len - 1))
for i in range(1, arg_len):
    print("{}: {}".format(i, sys.argv[i]))
