#!/usr/bin/python3
"""
This module provides a function that writes a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number
    of characters written.

    Args:
        filename (str): The file path.
        text (str): The string to write.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
