#!/usr/bin/python3


"""
This module creates class Rectangle
with private attribute 'width' and 'height'
"""


class Rectangle:
    """initialize class attributes:
      to count number of instances
      to print rectangle with any symbol"""

    number_of_instances = 0
    print_symbol = "#"

    """initialize the instance of Rectangle class
    with attribute width and height"""

    def __init__(self, width=0, height=0):
        """Init method

        Keyword Arguments:
            width [int] -- widht of triangle default: 0
            height [int] -- height of triangle default: 0
        """
        self.width = width
        self.height = height

        """public class attribute number_of_instances"""
        Rectangle.number_of_instances += 1

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

    """return area of the rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """return perimeter of a rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """return printable repr of a rectangle
        ready to print with character #"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = ""
            for i in range(self.__height):
                """use the class attr print_symbol here"""
                rect += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rect += "\n"
        return (rect)

    def __repr__(self):
        """function repr to return the atributes of rectangle"""

        return "Rectangle(" + str(self.__width)+", "+str(self.__height) + ")"

    def __del__(self):
        """function that deletes an instance of a rectangle
        and decrement the number of instances by one"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new instance of Rectangle that is a square
        width == height == size
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))
