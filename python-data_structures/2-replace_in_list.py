#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    #element = my_list[idx]
    #element = new_element
    my_list[idx] = [new_element]
    new_list = my_list
    for idx in len(my_list) - 1:
        if idx < 0 and idx > len(my_list):
            return (my_list)
    return (new_list)
