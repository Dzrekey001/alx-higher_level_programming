#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0
    try:
        for i in range(x):
            list_len += 1
            print("{:d}".format(my_list[i]), end="")
    except IndexError:
        pass
    finally:
        print()
        return (list_len)

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
