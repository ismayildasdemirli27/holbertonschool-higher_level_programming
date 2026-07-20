#!/usr/bin/env python3
"""
Module for Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius=0):
        """Initialize the circle with a radius."""
        self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle using math.pi."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle using math.pi."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height."""
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Calculate the area of the rectangle."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print the area and perimeter of a shape relying on duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
