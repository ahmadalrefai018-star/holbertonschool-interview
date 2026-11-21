#!/usr/bin/python3
"""Calculate the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Return the number of exposed edges of the island."""
    perimeter = 0

    for row_index, row in enumerate(grid):
        for col_index, cell in enumerate(row):
            if cell == 0:
                continue

            perimeter += 4
            if row_index > 0 and grid[row_index - 1][col_index] == 1:
                perimeter -= 2
            if col_index > 0 and row[col_index - 1] == 1:
                perimeter -= 2

    return perimeter
