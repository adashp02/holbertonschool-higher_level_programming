#!/usr/bin/python3


"""
This module creates class Square
with private attribute 'size'
"""


class Square:

    """initialize the instance of Square class
    Args:
        size (int): The size of the new square.
        position (int, int): The position of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
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
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        """set value"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """return the area of the suare"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square"""
        
        pozzy = self.__position
        sizzy = self.__size
        if self.__size is 0:
            print()
        else:
            for _ in range(pozzy[1]):
                print()
            for _ in range(sizzy):
                for j in range(sizzy + pozzy[0]):
                    if j < pozzy [0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
