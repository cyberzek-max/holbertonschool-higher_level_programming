#!/usr/bin/python3
"""
This module defines a Student class with a method
to return a dictionary representation of its instance.
"""


class Student:
    """
    Student class with public attributes first_name,
    last_name, and age.
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

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance.

        Returns:
            dict: Dictionary with all instance attributes.
        """
        return self.__dict__.copy()
