# 143. Reorder List

Read both the sol

- **sol1**: brute force (my own)
- **sol2**: optimal reverse version (my own, independent). O(n) time, O(1) extra space

## sol1: brute force

- Count the nodes, then repeatedly walk from `start` to the current last node and splice it in after `start`.
- After each splice, the remaining gap shrinks by 2 (`cnt -= 2`).
- At the end, `start.next = None` cuts the leftover pointer / self-loop.
- Walk lengths are (n-1) + (n-3) + (n-5) + ... → O(n²) time.

## sol2: find middle → reverse second half → merge

1. **Find the middle** with slow/fast, both starting at `head`. `slow` ends at the **second** middle (3 in 1→2→3→4).
2. **Reverse** from `slow` to the end. The middle goes into the second half.
3. **Merge** by weaving one node from each half: `while end.next`.

### My version vs NeetCode

|                  | Mine                                                 | NeetCode                                             |
| ---------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| fast starts at   | `head`                                               | `head.next`                                          |
| slow ends at     | second middle (3 in 1→2→3→4)                         | first middle (2 in 1→2→3→4)                          |
| reverse from     | `slow` (middle goes in the 2nd half)                 | `slow.next` (middle stays in the 1st half)           |
| halves cut?      | No. 1st half still points into the reversed half      | Yes. `slow.next = None` makes two separate lists      |
| merge loop       | `while end.next`                                     | `while second`                                       |

**Why NeetCode can use `while second`:** after the cut there are two separate lists, and the second is never longer than the first. Each pass takes one node from `second`. Once it's `None`, every node has been placed, and any leftover node of `first` is already at the end with `next = None`.

```
first:  1 → 2 → 3          second: 5 → 4
```

**Why mine needs `while end.next`:** the list is never cut, so both halves end at the **same** node.

```
first:  1 → 2 ↘
                 3 → None
second: 5 → 4 ↗
```

Node 3 is the last node of both halves. Weaving 3 into itself breaks things. `end.next is None` exactly when `end` is that shared node, so the loop stops one step earlier.

**What goes wrong with `while end`** (trace 1→2→3→4, start=1, end=4):

| pass | start | end | effect                                              |
| ---- | ----- | --- | --------------------------------------------------- |
| 1    | 1     | 4   | 1→4→2. Fine                                         |
| 2    | 2     | 3   | `2→3`, then `end.next = temp_start` gives 3→3, a **self-loop** |

The result is a cycle, so LeetCode hangs or fails. For odd lengths `while end` happens to come out right, so the bug passes some tests and fails others.

> **Rule:** the loop's stopping condition must match how you split the list.
> If you cut it apart, loop until the shorter list is `None`. If the halves share a tail node, stop before reaching it.

## Cleanup TODO

- `slef` → `self`, `revreseSol` → `reverseSol`, delete the commented-out prints.
- Add the guard `if not head or not head.next: return`.

## Open complexity questions

- sol2: how many times does each of the 3 loops run, in terms of n? How do they combine? Extra space?
- sol1: what Big-O is (n-1) + (n-3) + (n-5) + ...?
