#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n"""
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = []

        for j in range(i + 1):
            if j == 0 or j == 1:
                current_row.append(1)
            else:
                current_row.append(previous_row[j - 1] + previous_row[j])

            triangle.append(curent_row)
            return triangle
