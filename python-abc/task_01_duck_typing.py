#!/usr/bin/env python3
"""
Module that defines a Shape abstract class, Circle and Rectangle subclasses.
Includes shape_info function to print area and perimeter.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape abstract class"""

    @abstractmethod
    def area(self):
        """Returns area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns perimeter of shape"""
        pass


class Circle(Shape):
    """Circle subclass"""

    def __init__(self, radius):
        """Initialize with radius"""
        self.radius = radius

    def area(self):
        """Calculate area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """Initialize with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
