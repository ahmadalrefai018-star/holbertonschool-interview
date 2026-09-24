#!/usr/bin/python3
"""Generate Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's Triangle."""
    if n <= 0:
        return []

    triangle = []

    for row_index in range(n):
        row = [1] * (row_index + 1)

        for column in range(1, row_index):
            row[column] = (triangle[row_index - 1][column - 1]
                           + triangle[row_index - 1][column])

        triangle.append(row)

    return triangle
