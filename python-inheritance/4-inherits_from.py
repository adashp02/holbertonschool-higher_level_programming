#!/usr/bin/python3
"""function that returns True if
an object is an instance of a class inherited
fr_m a specified class
"""


def inherits_from(obj, a_class):
    """function validating that obj is an instance
    of a class inherited fr_m a specified class

    Args:
        obj - object to be evaluated
        a_class - class to be checked against

    Returns:
        False or True
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    return False
