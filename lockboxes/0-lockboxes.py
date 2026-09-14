#!/usr/bin/env python3
"""Lockboxes"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = {0}
    keys_to_check = [0]

    while keys_to_check:
        current = keys_to_check.pop()

        for key in boxes[current]:
            if key < n and key not in visited:
                visited.add(key)
                keys_to_check.append(key)

    return len(visited) == n
