# [3090. Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

**Category:** Sliding Window
**Difficulty:** Easy
**Concepts:** gaps & grouping, sliding window, counting via index bounds

---

## Approach 1: Brute Force — Two Pass (O(n³))

Nested `i`, `j`, `k` loops — re-scan the window from scratch every time it grows.

### Bug found & fixed
Original had a stray `if d1[s[k]] > 2:` check right after the inner `while` loop, which threw `KeyError` on inputs like `"bcbbbcba"`.

Root cause: when the `while` loop exits *without* a break (no duplicate found), `k` has already incremented to `j+1` — one step outside the window — so `s[k]` isn't guaranteed to be a valid key in `d1` anymore.

Traced both exit paths and found this check was **fully redundant** with the existing `s1` flag — they always agree. Removed it.

**Takeaway:** when two conditions in code always evaluate the same way, that's not extra safety — it's a second source of truth that can silently go stale after a refactor. Keep the one that states intent clearly, delete the other.

### Complexity
- TODO — derive precisely (loop bound reasoning for i / j / k)

---

## Approach 2: Optimal — One Pass (O(n))

Status: **not yet derived.**

Core idea to build out: count valid windows via gap `d` between repeated characters, using the relation `n - d`.

7-step derivation structure being used:
1. Why count `i` — each valid `i` maps to exactly one pair with gap `d`
2. What makes `i` valid
3. Lower bound on `i`
4. Upper bound on `i`
5. Inclusive count of valid `i` values
6. Simplify to `n - d`
7. Conclusion

---

## Personal Notes

**Date started:**
**Time taken:**
**Independent vs. hints needed:**

**Questions I asked myself / Claude:**
-

**Random back-and-forth / life stuff during this session:**
-

**How I felt about it:**
-
