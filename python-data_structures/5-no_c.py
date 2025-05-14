#!/usr/bin/python3
def no_c(my_string):
    #filtering method with .join
    result = ''.join([char for char in my_string if char.lower() != 'c'])
    return (result)
