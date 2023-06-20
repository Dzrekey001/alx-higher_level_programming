#!/usr/bin/python3
"""This class is the base of other classes"""

import json
import os


class Base:
    """ Base class for all other classes
        Attributes:
            __nb_objects (int): The number of instantitated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Intantiates a new instance
            Args:
                id (int): the identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a Json representation
        Args:
            list_dictionaries (list): list containing values:
        Returns:
            json represation
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON representation to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return the deserialize json string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instance from a dictionary of attribute"""
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        else:
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp
