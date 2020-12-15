#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        for i in range(len(tuple_a), 2):
            tuple_a = tuple_a + (0,)
    if len(tuple_b) < 2:
        for i in range(len(tuple_b), 2):
            tuple_b = tuple_b + (0,)
    res = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return res
