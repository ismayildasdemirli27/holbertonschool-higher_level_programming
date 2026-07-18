#!/usr/bin/env python3
"""Module for pickling custom classes."""
import pickle


class CustomObject:
    """A custom object class to demonstrate pickling."""

    def __init__(self, name, age, is_student):
        """Initializes the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
