#!/usr/bin/python3
"""
This module provides a function that writes a Python object
to a file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): Path to the file where JSON will be written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
