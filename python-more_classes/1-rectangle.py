#!/usr/bin/python3


"""
This module creates class Rectangle
with private attribute 'width' and 'height'
"""


class Rectangle:

    """initialize the instance of Rectangle class
    with attribute width and height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """getter - retrieve width of Rectangle"""
    @property
    def width(self):
        return (self.__width)

    """setter - set the value of width"""
    @width.setter
    def width(self, value):

        """if size is not an integer"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        """width is a private attribute"""

        self.__width = value

    """getter - retrieve height of Rectangle"""
    @property
    def height(self):
        return (self.__height)

    """setter - set the value of height"""
    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
