#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # If a tuple is smaller than 2, use the value 0 for each missing integer
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    # If a tuple is bigger than 2, use only the first 2 integers
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    # The first element is sum of the first element of each argument
    first_element = tuple_a[0] + tuple_b[0]
    # The second element is sum of the second element of each argument
    second_element = tuple_a[1] + tuple_b[1]
    # Returns a tuple with 2 integers
    return (first_element, second_element)
