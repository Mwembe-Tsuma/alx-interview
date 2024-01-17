#!/usr/bin/python3
"""Minimum operations needed to result in nH char is a file"""


def minOperations(n):
    """Implementation for the minOperations method"""
    if n <= 1:
        return 0

    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 2
        current += clipboard

    return operations
