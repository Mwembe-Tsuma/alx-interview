#!/usr/bin/python3
"""Minimum operations needed to result in nH char is a file"""


def minOperations(n):
    """Implementation for the minOperations function"""

    if not isinstance(n, int):
        return 0
    operations = 0
    num_char = 1
    #clipboard = 0  # Initialize clip_board here

    while n > num_char:
        if n >= num_char * 2:
            clipboard = num_char
            operations += 1
        num_char += clipboard
        operations += 1

        if n > num_char:
            num_char += clipboard
            operations += 1

    return operations
