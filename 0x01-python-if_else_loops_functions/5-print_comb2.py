#!/usr/bin/python3
for i in range(100):
    if i != 99:
        if i <= 9:
            i = str(0) + str(i)
        print(f"{i},", end=" ")
    else:
        print(f"{i}")
