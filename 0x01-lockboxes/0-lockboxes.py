#!/usr/bin/python3
"""A Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Implemenation"""
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        curr_box = stack.pop()

        for key in boxes[curr_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
