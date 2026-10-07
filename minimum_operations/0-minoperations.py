#!/usr/bin/python3
"""Calculate the minimum number of operations."""


def minOperations(n):
    """Return the minimum operations required to produce n characters."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
