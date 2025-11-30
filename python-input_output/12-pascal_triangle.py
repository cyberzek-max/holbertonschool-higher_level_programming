#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows

    Returns:
        list[list[int]]: Pascal's triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    # Example usage
    test_values = [5, 1, 0, 10]
    for n in test_values:
        print(f"n = {n}")
        for row in pascal_triangle(n):
            print(row)
