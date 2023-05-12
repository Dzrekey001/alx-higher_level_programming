#!/usr/bin/python3
import sys

l_args = len(sys.argv) - 1

if l_args == 0:
    print("0 arguments.")
elif l_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(l_args))
for i in range(l_args):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
