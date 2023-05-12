#!/usr/bin/python3
import sys
argument = sys.argv
arg_len = len(argument)

if arg_len == 1:
    print("{} arguments.".format(arg_len - 1))
elif arg_len == 2:
    print("{} argument.".format(arg_len - 1))
else:
    print("{} arguments:".format(arg_len - 1))
for i in range(1, arg_len):
    print("{}: {}".format(i, argument[i]))
