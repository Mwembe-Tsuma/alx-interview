#!/usr/bin/python3
"""Prime Game implementation."""


def isWinner(x, nums):
    """
    Determine the winner of each game played x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the range for each round.

    Returns:
        str or None: Name of the player that won the most rounds.
        None if the winner cannot be determined.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_score = 0
    maria_score = 0

    for i in nums:
        prime_flags = [1] * (i + 1)

        prime_flags[0], prime_flags[1] = 0, 0

        for j in range(2, len(prime_flags)):
            remove_multiples(prime_flags, j)

        if sum(prime_flags) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None


def remove_multiples(prime_flags, prime):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.
    """
    for i in range(2, len(prime_flags)):
        try:
            prime_flags[i * prime] = 0
        except IndexError:
            break
