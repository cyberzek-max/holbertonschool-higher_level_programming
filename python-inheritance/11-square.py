#!/usr/bin/python3
"""Square class that inherits from Rectangle."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a square with a private size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
