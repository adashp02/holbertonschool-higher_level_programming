#!/usr/bin/python3


"""
This module creates class Square
with private attribute 'size'
"""


class Square:

    """initialize the instance of Square class
    with attribute size"""

    def __init__(self, size=0):
        
        """getter - get the size of the square"""
        @property
        def size(self):
            return (self.__size)

        """setter - same name as attribute"""
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")

            elif value < 0:
                raise ValueError("size must be >= 0")
            """size is a private attribute"""
            self.__size = value

    def area(self):
        """return the area of the suare"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square"""
        if self.__size is 0:
            print()
        else:
            for col in range(self.__size):
                for row in range(self.__size):
                    print("#", end="")
                print()

