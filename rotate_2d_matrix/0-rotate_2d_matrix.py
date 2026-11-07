#!/usr/bin/python3
"""Rotate a square matrix 90 degrees clockwise in-place."""


def rotate_2d_matrix(matrix):
    """Rotate matrix in-place without returning a value."""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
