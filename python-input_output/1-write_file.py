#!/usr/bin/python3
"""
This module provides a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number
    of characters written.
    Args:
        filename (str): The path to the file to write to.
        text (str): The content to write into the file.
    Returns:
        int: The number of characters successfully written.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
