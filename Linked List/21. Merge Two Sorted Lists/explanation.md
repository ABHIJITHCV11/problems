# 21. Merge Two Sorted Lists

Independent and optimal.

## Approach

- Dummy node + `tail` pointer.
- While both lists have nodes, attach the smaller one and advance that list.
- Attach whichever list is left over (it's already sorted).
- Return `dummy.next`.

O(n + m) time, O(1) extra space (just relinks existing nodes).

## Used later

Merge K Sorted Lists = a heap + this merge.

TODO: add solution file.
