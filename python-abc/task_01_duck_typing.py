#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""
this is global enviroment
"""


class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        if self.radius < 0:
            return "Perimeter should handle negative radius"
        return 2 * pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
