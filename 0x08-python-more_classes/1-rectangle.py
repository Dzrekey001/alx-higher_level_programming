#!/usr/bin/python3
"""A class that defines a rectangle by:
    (based on 0-rectangle.py)
"""


class Rectangle:
    """Define the class for the rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter/setter property for self.width"""
        return (self._width)

    @width.setter
    def width(self, value):
        if type(self.value) is not int:
            raise TypeError("width must be an integer")

        if self.value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """getter/setter property for self.height"""
        return (self._height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if type(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
