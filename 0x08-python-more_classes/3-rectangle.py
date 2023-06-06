#!/usr/bin/python3
"""A class for Rectangle that defines a rectangle by:
    (base on 1-retangle.py)
"""


class Rectangle:
    """Define the class for the rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes intanstance variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter/setter property for self.width"""
        return (self._width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise TypeError("height must be >= 0")
        self_width = value

    @property
    def height(self):
        """getter/setter property for self.height"""
        return (self._height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

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
        return string
