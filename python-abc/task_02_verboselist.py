#!/usr/bin/env python3
"""
Module that defines the VerboseList class.
Extends the built-in Python list to print notifications upon modification.
"""


class VerboseList(list):
    """A custom list class that prints notifications when modified."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with an iterable and prints a notification."""
        items_added = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Prints a notification, then removes the item from the list."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification, then pops the item at the given index."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
