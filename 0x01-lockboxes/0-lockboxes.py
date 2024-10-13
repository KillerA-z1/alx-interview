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
