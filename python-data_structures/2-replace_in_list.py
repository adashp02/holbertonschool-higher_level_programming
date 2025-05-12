#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    #element = my_list[idx]
    my_list[idx] = [element]
    for idx in len(my_list) - 1:
        if idx < 0 and idx > len(my_list) - 1:
            return (my_list)
    return (new_list)
