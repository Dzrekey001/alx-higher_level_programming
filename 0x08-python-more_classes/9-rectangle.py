#!/usr/bin/python3
"""A class for Rectangle that defines a rectangle by:
    (base on 1-retangle.py)
"""


class Rectangle:
    """Define the class for the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter/setter property for self.width"""
        return (self._width)

    @width.setter
    def width(self, value):
        if type(self.value) is not int:
            raise TypeError("width must be an integer")

        if self.value < 0:
            raise TypeError("height must be >= 0")

    def area(self):
        """A public instance that defines area of rectangle"""
        return (self._width * self.height)

    def perimeter(self):
        """A public instance that returns the perimeter of rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return ((self._width * 2) + (self_heigth * 2))

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a string when an instance has been deleted"""
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square w/ h==w==size"""
        return cls(size, size)
