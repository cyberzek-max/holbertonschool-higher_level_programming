#!/usr/bin/python3
"""
This module provides a function that returns the JSON
representation of a Python object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object.

    Args:
        my_obj: Any Python object that can be serialized to JSON.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
