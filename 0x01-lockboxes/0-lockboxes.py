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
    opened = set([0])  # Start with the first box opened
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key not in opened:
                opened.add(key)
                keys.append(key)

    return len(opened) == n
