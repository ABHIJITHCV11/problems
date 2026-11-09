# 206. Reverse Linked List

Solved both iterative and recursive (1 hint).

## Iterative

```
prev, curr = None, head
while curr:
    temp = curr.next   # save next before breaking the link
    curr.next = prev   # flip the pointer
    prev = curr
    curr = temp
return prev            # new head
```

O(n) time, O(1) space.

## Recursive

Reverse the rest of the list, then hook the current node onto its end
(`head.next.next = head`, `head.next = None`). O(n) time, O(n) call stack.

## Used later

- Reorder List: reversing the second half.
- Reverse Linked List II / Reverse Nodes in K Group: reversing just one section.

TODO: add solution file(s).
