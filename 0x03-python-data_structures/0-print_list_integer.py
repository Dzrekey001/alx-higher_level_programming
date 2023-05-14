#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        if type(num) == int:
            print("{}".format(num))
