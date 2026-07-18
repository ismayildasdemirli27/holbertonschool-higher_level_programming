#!/usr/bin/python3
"""This module returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object."""
    return obj.__dict__
