#!/usr/bin/python3
"""
the class BaseGeometry:
- area :
- interger_validator:
"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
