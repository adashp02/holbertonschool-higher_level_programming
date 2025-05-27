#!/usr/bin/python3
"""importing class BaseGeometry from another file"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        """initialize new instance of Rectangle

        Args:
        width (int): width of a new rectangle
        height (int) height of a new rectangle"""

        """width and height are positive ints validated
        by Int validator that's inherited
        they are also private"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)
    """method area to return the area of the rectangle"""

    """magic method __str__ to return a string to print 
    in a specified format"""

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


