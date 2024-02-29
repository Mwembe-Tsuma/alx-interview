#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Make change"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    result = 0

    for coin in coins:
        num_coins = total // coin

        result += num_coins
        total -= num_coins * coin

    if total != 0:
        return -1

    return result
