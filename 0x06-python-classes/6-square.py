#!/usr/bin/python3
"""a cass definition of a square"""


class Square(object):
    """square class with private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of class instance attribute
        Args:
             size (int): size of the square
             position (int): position of the square
            Return: None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculate the area square
        Return:
        the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            the value of the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter of __size
        Args:
            size (int): the size of the square
        Return: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """a method to print out the square"""
        if self.size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for i in range(0, self.__position[0])]
                [print("#", end="") for j in range(0, self.__size)]
                print("")

    @property
    def position(self):
        self.__position = position

    @position.setter
    def position(self, position):
        if (len(position) != 2 or
            type(position) is not tuple or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = position
