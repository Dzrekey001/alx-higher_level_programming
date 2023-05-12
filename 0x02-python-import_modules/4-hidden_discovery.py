#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = sort(dir(hidden_4))
    for name in names:
        if name[:2] != "__":
            print(name)
