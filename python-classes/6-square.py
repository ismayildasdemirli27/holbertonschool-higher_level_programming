#!/usr/bin/python3
"""
6-square module.
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #,
        using the position coordinates.
        """
        if self.__size == 0:
            print()
            return

        for y in range(self.__position[1]):
            print()

        for x in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
