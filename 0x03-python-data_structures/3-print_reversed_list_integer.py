#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = [None] * len(my_list)
    for i in range(0, len(my_list)):
        rev_list[i] = my_list[(-1*(i+1))]
    for i in rev_list:
        print("{:d}".format(i))
