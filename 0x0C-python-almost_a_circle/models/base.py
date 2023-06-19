#!/usr/bin/python3

import json


class Base(object):
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
        if list_dictionaries is not None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save all intance value to json"""

        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                content = [tmp.to_dictionary() for tmp in list_objs]
                jsfile.write(Base.to_json_string(content))
