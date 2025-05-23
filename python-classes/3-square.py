#!/usr/bin/python3


"""
This module creates class Square
with private attribute 'size'
"""


class Square:

    """initialize the instance of Square class
    with attribute size"""

    def __init__(self, size=0):

        """if size is not an integer"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        """size is a private attribute"""

        self.__size = size
        def area(self):
            return (self.size ** 2)
