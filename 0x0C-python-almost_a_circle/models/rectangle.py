#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ Defines Rectangle class that Inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle:
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (id): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter/setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """getter/setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """getter/setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter/setter for y"""
        return self.__y

    @width.setter
    def y(self, value):
        self.__y = value
