#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    
    triangle = []  # This will store the triangle row by row

    for row_num in range(n):
        row = [1]  # First element is always 1
        if triangle:
            last_row = triangle[-1]
            # Build the middle values by adding adjacent elements from the previous row
            for i in range(1, len(last_row)):
                row.append(last_row[i - 1] + last_row[i])
            row.append(1)  # Last element is always 1
        triangle.append(row)
