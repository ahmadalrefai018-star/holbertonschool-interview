#!/usr/bin/python3
"""Determine the overall winner of the Prime Game."""


def isWinner(x, nums):
    """Return the player with the most wins, or None if tied."""
    if x < 1 or not nums or x > len(nums):
        return None

    rounds = nums[:x]
    limit = max(1, max(rounds))

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    prime = 2
    while prime * prime <= limit:
        if is_prime[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                is_prime[multiple] = False
        prime += 1

    prime_counts = [0] * (limit + 1)
    for number in range(2, limit + 1):
        prime_counts[number] = prime_counts[number - 1] + is_prime[number]

    maria_wins = sum(prime_counts[max(0, n)] % 2 for n in rounds)
    ben_wins = x - maria_wins

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
