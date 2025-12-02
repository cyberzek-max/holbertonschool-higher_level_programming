#!/usr/bin/python3
"""
The programme return:
- True
- False
"""


def inherits_from(obj, a_class):
    """
    function
    """
    return not type(obj) is a_class and isinstance(obj, a_class)
