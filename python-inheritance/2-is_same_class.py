#!/usr/bin/python3
"""function that returns True if
an object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """function validating that obj is an instance
    of a_class

    Args:
        obj - object to be evaluated
        a_class - class to be checked against

    Returns:
        False or True
    """
    if type(obj) is a_class:
        return True
    return False
