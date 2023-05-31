#!/usr/bin/python3
import math
"""a magicClass"""


class MagicClass:
    """a class to calculate the arrea and circuference"""

    def __init__(self, radius=0):
        """class Instance Attribute
        Args:
            radius (int): radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """return the area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """return the circumference"""
        return 2 * math.pi * self.__radius
