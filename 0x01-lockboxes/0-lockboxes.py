#!/usr/bin/python3
"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    if not isinstance(boxes, list):
        return False

    if len(boxes) == 0:
        return False

    keys = [0]
    opened = set(keys)

    for key in keys:
        for new_key in boxes[key]:
            if new_key not in opened and new_key < len(boxes):
                opened.add(new_key)
                keys.append(new_key)

    return len(opened) == len(boxes)
