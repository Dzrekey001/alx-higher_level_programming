#!/usr/bin/python3
"""A class that Invert the meaning to the equal ==,
    and not equal != sign
"""


class MyInt(int):
    """Inherits form int"""
    def __init__(self, integer):
        """Initialize instance attributes"""
        self.integer = integer

    def __eq__(self, other):
        """Invert the equal sign"""
        return (self.integer != other)

    def __ne__(self, other):
        """Invert the not equal sign"""
        return (self.integer == other)
