# 141. Linked List Cycle

Independent and optimal.

## Floyd's cycle detection (slow/fast)

- `slow` moves 1 step, `fast` moves 2.
- If there's a cycle, fast eventually catches up to slow (`slow == fast`) → `True`.
- If fast hits the end (`not fast or not fast.next`) → `False`.

O(n) time, O(1) space (vs O(n) with a visited set).

## Used later

- Reorder List: the same slow/fast walk finds the middle.
- Find The Duplicate Number: Floyd's on an array.

TODO: add solution file.
