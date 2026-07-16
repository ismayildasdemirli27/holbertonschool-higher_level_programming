#!/usr/bin/env python3
"""Module defining Shape, Circle, and Rectangle classes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a generic shape."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Prints the area and perimeter of a given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

