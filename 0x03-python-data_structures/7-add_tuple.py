#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    try:
        tup_a_0 = tuple_a[0]
    except error:
        tup_a = 0
    try:
        tup_a_1 = tuple_a[1]
    except error:
        tup_a_1 = 0
    try:
        tup_b_0 = tuple_b[0]
    except error:
        tup_b_0 = 0
    try:
        tup_b_1 = tuple_b[1]
    except error:
        tup_b_1 = 0

    indx_0 = tup_a_0 + tup_b_0
    indx_1 = tup_a_1 + tup_b_1
    new_tuple = [indx_0, indx_1]
    return (tuple(new_tuple))
