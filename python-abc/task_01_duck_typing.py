#!/usr/bin/env python3
"""Module for shapes and duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Shape info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

