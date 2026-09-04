# 424. Longest Repeating Character Replacement

## Approach: Sliding Window (variable size) + character frequency map

Maintain a window `[l, r]` and a frequency map of characters inside it.
Track `max_frq`, the highest frequency of any single character seen so far
within the window.

A window of length `r-l+1` is valid if we can turn it into a string of one
repeated character using at most `k` replacements — i.e. every character
other than the most frequent one gets replaced. That cost is:

```
r - l + 1 - max_frq
```

If that cost exceeds `k`, the window is invalid, so shrink it from the left
(`l += 1`, decrementing the frequency of the character leaving the window)
until it's valid again. After each expansion of `r`, record the max window
length seen.

## Key insight: `max_frq` never needs to shrink

`max_frq` is only ever updated upward (when the new right character's count
exceeds it) and is never recalculated downward when the window shrinks.
This looks like a bug — a shrunk window could have a smaller true max
frequency than `max_frq` claims — but it doesn't matter: the window can
never shrink below the largest valid window already found. A stale
(too-high) `max_frq` can only cause the window to stay the same size or
grow again once a matching character reappears; it can never report a
window length larger than one that was actually achievable. So `max_len`
stays correct even though `max_frq` is "wrong" mid-way through.

## Trace: `s = "AACBCBBB"`, `k = 1`

| window | check: `len - max_frq > k` | valid? | action |
|---|---|---|---|
| A       | 1-1 > 1? | F | r+1 |
| AA      | 2-2 > 1? | F | r+1 |
| AAC     | 3-2 > 1? | F | r+1 |
| AACB    | 4-2 > 1? | T | invalid → l+1 |
| ACB     | 3-2 > 1? | F | r+1 (window itself isn't a valid replacement-of-1 substring, but the size is still ≤ the max already found, since `max_frq` is stale) |
| CB      | 2-2 > 1? | F | r+1 |
| CBB     | 3-2 > 1? | F | r+1 |
| CBBB    | 4-3 > 1? | F | r+1 |

Loop ends. `max_len = 4` (from window `AACB`/`CBBB`).

## Complexity

- Time: O(n) — each index enters/leaves the window at most once.
- Space: O(1) — at most 26 lowercase/uppercase letters in the frequency map.
