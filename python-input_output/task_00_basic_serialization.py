#!/usr/bin/env python3
"""Basic serialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes JSON data from a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
