#!/usr/bin/env python3
"""
Module that defines the CountedIterator class.
Keeps track of the number of items that have been iterated over.
"""


class CountedIterator:
    """
    Custom iterator class that counts the number of fetched items.
    """

    def __init__(self, some_iterable):
        """
        Initializes the iterator object and the counter.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the original iterator and increments
        the counter. Raises StopIteration when no items are left.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
