#!/usr/bin/python3
"""
Prime Game implementation.
"""


def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(limit):
    """
    Generate a list of prime numbers up to the given
    limit using the Sieve of Eratosthenes.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def isWinner(x, nums):
    """
    Determine the winner of each game played x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers.

    Returns:
        str or None: Name of the player that won the most rounds.
        None if the winner cannot be determined.
    """
    def play_round(n):
        """Function to determine winner"""
        primes = sieve_of_eratosthenes(n)
        moves = 0

        while n > 1:
            if is_prime(n):
                moves += 1
                n -= 1
            else:
                largest_prime = max(p for p in primes if p <= n)
                moves += 1 + n // largest_prime
                n = largest_prime - 1

        return moves % 2

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        winner = play_round(num)
        if winner == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
