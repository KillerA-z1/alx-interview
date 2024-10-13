#!/usr/bin/python3
"""
canUnlockAll(boxes)

Determines if all the boxes can be opened.

Parameters:
    boxes (list of list of int): A list of lists where each sublist represents
    a box and contains keys to other boxes.

Returns:
    bool: True if all boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop(0)
        if key < n and key not in opened:
            if key not in opened:
                opened.add(key)
                keys.extend(boxes[key])

    return len(opened) == n
