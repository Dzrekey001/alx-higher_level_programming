#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0
    try:
        for element in my_list:
            list_len += 1

        for i in range(x):
            print({":d"}.format(element[i]), end="")
    except IndexError:
        break
    finally:
        print()
        return (list_len)
