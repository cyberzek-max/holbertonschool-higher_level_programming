#!/usr/bin/python3
"""
Rectangle module - defines a rectangle with width, height,
area, perimeter, string representation using print_symbol,
eval-compatible repr, instance deletion message, and
tracking number of instances.
"""


class Rectangle:
    """A class representing a rectangle."""

    number_of_instances = 0  # Tracks number of Rectangle instances
    print_symbol = "#"       # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle represented with print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)  # Ensure any type can be used
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string to recreate the rectangle using eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
