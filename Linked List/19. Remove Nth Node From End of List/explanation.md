# 19. Remove Nth Node From End of List

Read both the sol
Two pass vs one pass

Both are in `solution1.py` (`twoPass` and `onePass`).

## Key tricks

- **Dummy node** (`dummy = ListNode(0, head)`): removing the head becomes a normal case, and you always return `dummy.next`.
- To delete a node, stop at the node **before** it and do `curr.next = curr.next.next`.

## twoPass

1. Count the nodes (`cnt`).
2. Walk `cnt - n` steps from `dummy`. That lands on the node before the target.
3. Skip the target.

## onePass: fast/slow pointers with a fixed gap

- Unlike Reorder List / Cycle, where fast moves 2x, here the **gap between the pointers is fixed**.
- `slow = dummy`, `fast = head`. Move `fast` n steps ahead.
- Move both together until `fast` is `None`. `slow` then sits right before the node to remove.
- `slow.next = slow.next.next`.

## Open complexity question

- Time and extra space for each version? (Both are a single walk of the list in Big-O terms.)
