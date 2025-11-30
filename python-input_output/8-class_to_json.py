#!/usr/bin/python3
"""
This module defines a function that returns the dictionary
representation of a class instance suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a class instance
    with only simple data structures.

    Args:
        obj: The class instance.

    Returns:
        dict: Dictionary containing all instance attributes.
    """
    return obj.__dict__.copy()
