#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to a file using JSON

    Args:
        my_obj (obj): object to be written.
        filename: a text file to be write the obj into.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
