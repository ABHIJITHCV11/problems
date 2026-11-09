# 2. Add Two Numbers

Proud of my sol yeyyyy

Independent and optimal.

Digits are stored in reverse order (2→4→3 = 342). Return the sum in the same format.

## Approach

- Dummy node + `curr` pointer to build the result.
- Each step: `total = digit1 + digit2 + carry`, new node gets `total % 10`, `carry = total // 10`.
- Use 0 for a list that has run out, and only advance a list if it's still there.

## The key line: `while l1 or l2 or carry`

That one condition handles both tricky cases:

- **Different lengths**: `l1 or l2` keeps the loop going after one list runs out.
- **Final carry** (5 + 5 = 10 → 0→1): `or carry` adds the last `1` node.

Many people miss the carry case and need a separate `if carry:` after the loop. This version doesn't.

## Optional cleanup

```python
digit1 = l1.val if l1 else 0
digit2 = l2.val if l2 else 0
```

## Open complexity questions

- Time in terms of m and n (the two lengths)? Hint: max number of loop runs, counting the extra carry pass.
- Space: the output list is required. Apart from that, any extra memory?
