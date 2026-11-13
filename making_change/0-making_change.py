#!/usr/bin/python3
"""Find the minimum number of coins needed to make change."""


def makeChange(coins, total):
    """Return the fewest coins needed, or -1 if total is unreachable."""
    if total <= 0:
        return 0

    denominations = {coin for coin in coins if coin <= total}
    if not denominations:
        return -1

    unreachable = total + 1
    minimum = [0] + [unreachable] * total

    for coin in denominations:
        for amount in range(coin, total + 1):
            candidate = minimum[amount - coin] + 1
            if candidate < minimum[amount]:
                minimum[amount] = candidate

    if minimum[total] == unreachable:
        return -1
    return minimum[total]
