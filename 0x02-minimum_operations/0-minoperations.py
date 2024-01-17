#!/usr/bin/python3
""" Minimum Operations needed to get n H characters """


def minOperations(n: int) -> int:
    """ Implementation for the minOperations method """
    paste_content = 'H'
    current_content = 'H'
    op_count = 0

    while len(current_content) < n:
        if n % len(current_content) == 0:
            op_count += 2
            paste_content = current_content
            current_content += current_content
        else:
            op_count += 1
            current_content += paste_content

    if len(current_content) != n:
        return 0

    return op_count
