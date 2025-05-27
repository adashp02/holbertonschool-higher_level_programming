#!/usr/bin/python3
"""importing class Rectangle from another file"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inherited from Rectangle"""

    def __init__(self, size):
        """initialize new instance of Square

        Args:
        size (int): size of a new square
        """

        """size is a positive int validated
        by Int validator that's inherited
        it's also private"""

        self.integer_validator("size", size)
        self.__size = size

    """method to return the area of the square"""
    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
