#!/usr/bin/env python3
"""
Module containing Shape abstract class, Circle and Rectangle subclasses,
and shape_info function for duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a generic shape."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Prints the area and perimeter of a given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
