#!/usr/bin/python3
"""
the class BaseGeometry:
- area :
- interger_validator:
"""

class BaseGeometry:
    """
    there are some comment
    """
    def integer_validator(self, name, value):
        if type(name) is not str:
            raise TypeError(f"{name} must be a string")

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
