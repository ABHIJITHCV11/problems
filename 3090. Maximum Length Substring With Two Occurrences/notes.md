# [3090. Maximum Length Substring With Two Occurrences](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

**Categories:** Triple loops,Sliding Window

**Difficulty:** Easy

**Concepts:** gaps & grouping, sliding window, counting via index bounds

---

## Approach 1: Brute Force

*1.maximumLengthSubstring.py*

### 1.1 How We Arrived at the Time Complexity

#### 1.1.1 Initial Intuition

First pass — the "trust me" version: three nested loops (`i`, `j`, `k`), and `k`'s work grows proportionally with the window size (j - i). So it's not just `n × n × n` from three loops blindly stacked — the inner loop's cost itself scales with how far apart `i` and `j` are. That intuition alone gets you to "it's roughly n³," but it's not rigorous — it doesn't say why it's exactly cubic and not, say, quadratic-log or something else entirely.

#### 1.1.2 Prerequisite: Counting Pairs With a Fixed Gap `d`

**Main thing: `j - i + 1` counts elements, `j - i` counts gaps.**

These look almost the same but mean different things:
- `j - i` = the *distance* between two indices — how many steps apart they are. This is a **gap**.
- `j - i + 1` = the *number of elements* in the inclusive range `[i, j]` — this is a **count**.

Example: if `i = 2` and `j = 5`, the elements are indices `2, 3, 4, 5` — that's 4 elements, and `5 - 2 + 1 = 4` ✅. But `5 - 2 = 3` is just the gap between them, not how many elements are there.

Mixing these up is an easy off-by-one trap — anywhere you're counting "how many things are in this window," reach for `j - i + 1`, not `j - i`. Same idea as **taking away apples vs. counting apples** — one measures a difference, the other measures a quantity.

(My gf explained this distinction to me — gap vs. count — and it's what made the off-by-one logic finally click.)

#### 1.1.3 The 7-Step Derivation

1. **What are we ultimately trying to find?**  
   For a fixed gap `d`, we want to know: how many pairs `(i, j)` have exactly this gap?
2. **Why does counting `i` answer that question?**  
   Every pair with gap `d` looks like `(i, i+d)` — once you pick `i`, `j` is automatically `i+d`. So each valid choice of `i` gives exactly one pair. That means the number of valid `i` values = the number of pairs with gap `d`. This is the whole reason we're about to count `i` — it's a stand-in for counting pairs.
3. **What makes an `i` "valid"?**  
   `i` needs two things to be true:
   - `i ≥ 0` (it's a string index, can't be negative) — lower bound.
   - `j = i + d` must also be a valid index, meaning `j ≤ n-1`. Substituting: `i + d ≤ n-1`, so `i ≤ n-1-d` — upper bound.
4. **So `i` can be any whole number between these two bounds.**  
   Lower bound: `0`. Upper bound: `n-1-d`.
5. **Count how many whole numbers fit between them (inclusive).**  
   Using the inclusive-counting rule (`upper − lower + 1`):
   ```
   (n-1-d) - 0 + 1
   ```
6. **Simplify.**  
   Subtracting `0` changes nothing: `(n-1-d) + 1 = n - d`.
7. **Conclusion.**  
   Count of valid `i` values = `n - d`. Since each `i` = one pair, **count of pairs with gap `d` = `n - d`.**

#### 1.1.4 Total Work Across All Gaps

Total work for one specific gap `d`: multiply count × cost:
```
(n - d)(d + 1)
```

Total work across all gaps — add this up for every `d` from `1` to `n-1`:
```
Total = Σ (d = 1 to n-1) (n - d)(d + 1)
```

Expand the product:
```
(n - d)(d + 1) = nd + n - d² - d
```

Split the sum into four separate sums:
```
Σ nd + Σ n - Σ d² - Σ d      (each summed for d = 1 to n-1)
```

Use known formulas for each piece (standard, memorizable identities):
- `Σ d = n(n-1)/2`
- `Σ d² = (n-1)n(2n-1)/6`
- `Σ n = n(n-1)` (n added to itself, n-1 times)
- `Σ nd = n · Σ d = n · n(n-1)/2`

Substitute and simplify (combine fractions over denominator 6, collect terms):
```
Total = n(n-1)(n+4) / 6
```

**Sanity check** against `n=6`: `(6 × 5 × 10) / 6 = 50` ✅ — matches hand-count.

Drop constants for Big-O (dominant term is `n × n × n / 6`):
```
O(n³)
```

That's the complete summation, done.

### 1.2 Proof vs. Solution?

Good distinction to ask about — they're related but not identical.
- This is a *derivation* — we started from the problem's structure and mechanically built up to a formula, checking it against real numbers along the way. It's rigorous, but it's not framed as a formal mathematical proof (which would typically use more formal notation, induction, or explicit justification for every algebraic step).
- If you wanted a formal *proof* that `Σd = n(n-1)/2`, for example, you'd typically prove it by mathematical induction — a structured technique: prove it's true for a base case (`n=1`), then prove that if it's true for `n`, it's true for `n+1`. That's a different, more formal exercise than what we did.

**Conclusion: O(n³).**

### 1.3 Bug Fix

Fixed it defensively at first (`if k <= j and d1[s[k]] > 2:`), then traced through both ways the `while` loop could end and found this new guard always agreed with a flag (`s1`) I already had — fully redundant. Killed the redundant one. Lesson: two conditions that always evaluate the same way isn't extra safety, it's a second source of truth that can drift out of sync after a future refactor.

---

## Personal Notes

**Date started:** 17-08-2026
**Time taken:**   6+ hrs
**Independent vs. hints needed:** many
