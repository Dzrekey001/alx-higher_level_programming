#!/usr/bin/python3
"""
    A class Student that defines a student
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        if type(attrs) is list:
            return {items: getattr(self, items) for items in attrs
                    if hasattr(self, items)}
        else:
            return self.__dict__
