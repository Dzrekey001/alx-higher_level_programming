#!/usr/bin/python3
"""This class is the base of other classes"""

import json


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
        if (list_dictionaries is not None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save all intance value to json"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as open_file:
            if list_objs is None:
                open_file.write("[]")
            else:
                string_rep = cls.to_json_string(
                        [objs.to_dictionary() for objs in list_objs])
                open_file.write(string_rep)
