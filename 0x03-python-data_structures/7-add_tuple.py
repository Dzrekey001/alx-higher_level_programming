#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        tup_a_0 = tuple_a[0]
    except:
        tup_a = 0
    try:
        tup_a_1 = tuple_a[1]
    except:
        tup_a_1 = 0
    try:
        tup_b_0 = tuple_b[0]
    except:
        tup_b_0 = 0
    try:
        tup_b_1 = tuple_b[1]
    except:
        tup_b_1 = 0

    indx_0 = tup_a_0 + tup_b_0
    indx_1 = tup_a_1 + tup_b_1
    new_tuple = [indx_0, indx_1]
    return (tuple(new_tuple))
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
