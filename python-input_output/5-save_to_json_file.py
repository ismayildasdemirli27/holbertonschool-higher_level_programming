#!/usr/bin/python3
"""This module provides a function to save an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
