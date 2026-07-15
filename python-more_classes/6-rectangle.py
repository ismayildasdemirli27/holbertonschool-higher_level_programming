#!/usr/bin/python3
"""
This module defines a Rectangle class.
It demonstrates the use of class attributes and instance deletion.
"""


class Rectangle:
    """
    Rectangle class with private instance attributes width and height,
    and a public class attribute number_of_instances.
    """
    
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ... Sizin əvvəlki tapşırıqlardan qalan metodlarınız (area, perimeter, __str__, __repr__ və s.) ...

    def __del__(self):
        """Prints a message and decrements instance count upon deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
