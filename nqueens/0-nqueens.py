#!/usr/bin/python3
"""Print every solution to the N queens puzzle."""

import sys


def solve_nqueens(n):
    """Find solutions by placing one queen in each row."""
    queens = []
    columns = set()
    diagonals_down = set()
    diagonals_up = set()

    def backtrack(row):
        """Try each safe column in the current row."""
        if row == n:
            print(queens)
            return

        for col in range(n):
            if (col in columns or
                    row - col in diagonals_down or
                    row + col in diagonals_up):
                continue

            queens.append([row, col])
            columns.add(col)
            diagonals_down.add(row - col)
            diagonals_up.add(row + col)

            backtrack(row + 1)

            queens.pop()
            columns.remove(col)
            diagonals_down.remove(row - col)
            diagonals_up.remove(row + col)

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
