#!/usr/bin/python3


"""
This module creates a new class BaseGeometry
"""


class BaseGeometry:
    """ public instance method """
    def area(self):
        """area not yet implemented"""
        raise Exception("area() is not implemented")

    """public unstance method"""
    def integer_validator(self, name, value):
        """
        validates value as int

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if not isinstance(value, int):
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
