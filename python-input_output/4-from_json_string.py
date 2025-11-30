#!/usr/bin/python3
"""
This module provides a function that converts a JSON
string into a corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The resulting Python data structure.
    """
    return json.loads(my_str)
