#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    element = my_list[idx]
    new_list = my_list
    for idx in len(my_list):
        if idx < 0 and idx > len(my_list) - 1:
            return (my_list)
    return (new_list) 
