#!/usr/bin/env python3
"""
Module demonstrating Mixins in Python.
Contains SwimMixin, FlyMixin, and Dragon classes.
"""


class SwimMixin:
    """A mixin class that provides swimming functionality."""

    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying functionality."""

    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon that can both swim and fly."""

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
