#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """abstract base class Shape"""

    @abstractmethod
    def area(self):
        """calculate the area of a shape

        Returns:
            float: area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """calculate the perimeter of a shape
        
        Returns:
            float: a perimeter of a shape
        """
        pass

class Circle(Shape):
    """class representing a circle, inherited from Shape"""

    def __init__(self, radius):
        self.radius = radius
        """initialize a circle with a radius
        
        Args:
            radius: float - radius of a circle
        """
    def area(self):
        return math.pi * self.radius ** 2
        """implement the area method from above
        with pi r **2 formula
        
        Returns: float
        """
    def perimeter(self):
        return 2 * math.pi * self.radius
        """implement the perimeter method from above
        with the math formula 2 pi r
        
        Returns: float
        """

class Rectangle(Shape):
    """class representing a rectangle inherited from Shape"""

    def __init__(self, width, height):
        """initialize rectangle with width and height
            
        Args: 
            width - float
            height - float
        """
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
        """implement area method

        Returns: 
            area of the rectangle(float)
        """
    def perimeter(self):
        return 2 * (self.width + self.height)
        """implement the perimeter method
                
            Returns:
                float - perimeter of the rectangle
        """
    def shape_info(shape):
        """Print area and perimeter of a shape
            this method evokes duck typing
            you can trust that the passed object
            adheres to the Shape interface. 
            
            Arg: shape (from Shape)
                object with area and perimeter methods
        """
        print("Area: {}".format(shape.area()))
        print("Perimeter: {}".format(shape.perimeter()))

    #Usage - test
    if __name__ == "__main__":
        circle = Circle(7)
        rectangle = Rectangle(4, 5)

        print("Circle:")
        shape_info(circle)
        #it should print area + perimeter of the circle

        print("\nRectangle:")
        shape_info(rectangle)
        #it should print area + perimeter of the rectangle
