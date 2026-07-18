#!/usr/bin/python3
"""This module provides a function to create an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file."""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
