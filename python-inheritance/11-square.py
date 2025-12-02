#!/usr/bin/python3
"""
write the class Square from Rectangle:
- area :
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    the class Square
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
