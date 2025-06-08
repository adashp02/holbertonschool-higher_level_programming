#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):

    """Args:
            my_str (str) - string to convert from JSON 
        Returns:
            (obj) python object (data structure)
    """

    return json.loads(my_str)

