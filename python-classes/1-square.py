#!/usr/bin/python3
"""
1-square module.
"""


class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size):
        """
        Initializes a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
