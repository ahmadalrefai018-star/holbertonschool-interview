#!/usr/bin/python3
"""Determine whether all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if every box is reachable from box zero."""
    if not boxes:
        return True

    opened = {0}
    pending = [0]

    while pending:
        box = pending.pop()

        for key in boxes[box]:
            if 0 <= key < len(boxes) and key not in opened:
                opened.add(key)
                pending.append(key)

    return len(opened) == len(boxes)
