#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints list in reverse"""
    rev_list = my_list[::-1] #reverse list by slicing
    for num in rev_list:
        print("{:d}".format(num))
