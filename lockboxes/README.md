# Lockboxes

Determine whether all boxes can be unlocked starting from box 0.

The solution explores reachable boxes using a stack and tracks opened
boxes with a set. Duplicate keys and keys outside the box range are ignored.

- File: `0-lockboxes.py`
- Function: `canUnlockAll(boxes)`
- Time complexity: O(n + k), where k is the total number of keys.
- Space complexity: O(n).
