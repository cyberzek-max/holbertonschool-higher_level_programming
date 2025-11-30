#!/usr/bin/python3
"""
This module defines a Student class with a method
to return a dictionary representation of its attributes.
"""


class Student:
    """
    Student class with public attributes first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary of the Student instance attributes.

        Args:
            attrs (list of str, optional): Only include these attributes.
                                           If None, include all attributes.

        Returns:
            dict: Dictionary of attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        result = {}
        for key in attrs:
            if key in self.__dict__:
                result[key] = self.__dict__[key]
        return result
