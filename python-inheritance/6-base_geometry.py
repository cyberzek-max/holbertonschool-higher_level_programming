#!/usr/bin/python3
"""Module defining BaseGeometry class with unimplemented area method."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Raise an exception for unimplemented area method."""
        raise Exception("area() is not implemented")
