#!/usr/bin/env python3
"""
Module defining a Shape abstract class, Circle and Rectangle subclasses,
and a shape_info function relying on duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for generic shapes."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter."""
        pass


class Circle(Shape):
    """Circle subclass representing a circle shape."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle subclass representing a rectangle shape."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
