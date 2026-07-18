#!/usr/bin/python3
"""This module defines a Student class with a filtered JSON representation."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        if type(attrs) is list and all(type(ele) is str for ele in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
