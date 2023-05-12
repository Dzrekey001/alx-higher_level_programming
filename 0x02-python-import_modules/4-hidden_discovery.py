#!/usr/bin/python3
import hidden_4
import sys

if __name__ == "__main__":
    names = sort(dir(hidden_4))
    for name in names:
        if not name.startswith("__"):
            print(name)
