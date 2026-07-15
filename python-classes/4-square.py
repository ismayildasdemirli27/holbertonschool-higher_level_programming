#!/usr/bin/python3
"""
4-square module.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        self.size = size

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

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
