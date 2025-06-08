#!/usr/bin/python3
"""returns the dictionary description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """Args:
        object (obj): a class
        
    Returns:
        JSON reprezentation of a class
        """
    return obj.__dict__
