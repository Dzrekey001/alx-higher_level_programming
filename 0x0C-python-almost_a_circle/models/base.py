#!/usr/bin/python3

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
