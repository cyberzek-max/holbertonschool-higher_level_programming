#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 text file
and print its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
