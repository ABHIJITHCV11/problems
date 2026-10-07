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

## Approach 2: Slide it

u tell me
how do i frame it

i got the idea already
l only increments if the next r makes the string have more than 2 repeating char
but incrementsing l is not eniough becuase it might not contribute to decraesing the count
so we check again
same trhing reapts

there are proerties of r also

but how to frame it
howto start

do i do with invarianets ?
does google,netfix,alsian etc interview work like that ?

Thought for 7s

Yes — invariants are exactly the right tool, and yes, this is genuinely how Google/Netflix/Amazon-tier interviews work. Not as a written formal proof — but the interviewer is listening for exactly this reasoning, spoken out loud, while or after you code. It's the single biggest thing that separates "wrote code that happens to pass" from "understands what they wrote." Let's build it properly.

The general template for a loop invariant argument:

State the invariant — what's always true, at the top of every loop iteration?
Initialization — is it true before the loop even starts?
Maintenance — does each operation inside the loop preserve it?
Termination — when the loop ends, what does the invariant + exit condition together tell you?

Now applied to your solution:

1. Invariant: At the start of every iteration, the window s[l:r] (everything strictly before index r) contains no character with count greater than 2, and d1 accurately reflects the counts of characters within that window.

2. Initialization: l = r = 0, d1 = {}. The window s[l:r] is empty. An empty window trivially has no character exceeding count 2. ✅ Invariant holds before we begin.

3. Maintenance — this is where your two branches earn their keep:

Growing branch (if): you only add s[r] into the window when d1[s[r]] <= 1 (or it's not present). So after incrementing, the count becomes at most 2 — never violates the "≤2" rule. Then r moves forward, extending the window by exactly one valid element. Invariant preserved.
Shrinking branch (elif): triggers when s[r] would push some character's count to 3 if added — meaning the current window is fine, but adding s[r] would break it. So instead, you shrink from the left: decrement d1[s[l]], move l forward. This is the key move — you're not fixing the violation caused by s[r], you're removing an element from the current valid window to make room, without ever letting the window contain a violation. r doesn't move here because you haven't decided yet whether s[r] can be safely added — that's still an open question, re-checked next iteration.

This is exactly the intuition you already had — "incrementing l might not immediately fix the count, so we check again" — you just need the word for it: you never advance r past a character until you're sure adding it keeps the invariant intact. The elif branch is a pure repair loop — it only runs when necessary, and it terminates because each run strictly decreases d1[s[l]] by 1, so eventually the specific offending character's count drops back to ≤1 (or the character is removed from the window's relevant range).

4. Termination: loop ends when r == len(s). At every point before that, max_length was only updated inside the growing branch — meaning it only ever captured window sizes that satisfied the invariant. So max_length is guaranteed to be the size of a valid window, and since every valid window was checked at some point (nothing skipped — r moves one step at a time), it's the maximum such window.

That's the full correctness argument. Notice — no induction, no heavy notation, just: invariant → holds at start → preserved by both branches → conclusion follows from the exit condition. That's the level of rigor real interviews want, delivered conversationally.

Your framing on the first part is exactly right — let's confirm it precisely, then tackle the second (bigger) question.

Part 1 — shrinking, confirmed:

When the window is invalid because s[r]'s count exceeds the limit, removing s[l]:

If s[l] ≠ s[r]: the offending count (s[r]'s count) is untouched. Window is still invalid. Loop continues, l advances again.
If s[l] == s[r]: you've just removed one of the actual duplicate occurrences. s[r]'s count drops. Window becomes valid again (or at least, that specific violation is resolved).

And here's why you're guaranteed to eventually hit that second case: the offending duplicate of s[r] is physically sitting inside the window [l, r] somewhere — it has to be, that's why the count is too high. Since l only ever moves rightward, one step at a time, it's guaranteed to eventually walk into and remove that exact duplicate. It can't skip over it. So the shrink loop is guaranteed to terminate in a bounded number of steps, not run forever removing useless characters.

Part 2 — your real question: how do we know we haven't missed a valid substring?

This is the completeness argument, and it's genuinely the more important half of the proof — correctness of shrinking alone doesn't guarantee you've found the global maximum. Here's the reasoning:

Claim: at every checkpoint (fixed r), the l your algorithm lands on is the smallest possible l such that [l, r] is still valid.

Why: you only ever shrink when currently invalid, and you stop shrinking the instant it becomes valid again — not one step more, not one step less. So l isn't just "a" valid left boundary — it's the tightest one, the furthest left you could possibly go while keeping [l, r] valid.

Why that's the key fact: for a fixed right end r, that window [l, r] — with l at its minimal value — is the longest possible valid substring that ends exactly at position r. Any smaller l (further left) would include the duplicate again and break validity. Any larger l would just be a shorter valid substring — not the maximum for that r.

Now the completeness step: every substring in the entire string, valid or not, has some rightmost character — some specific index r. That means every possible valid substring is accounted for by exactly one r value, and for that r, your algorithm has already computed the longest valid substring ending there. So any given valid substring's length is automatically ≤ the value your algorithm computed for its own r.

Since your loop visits every r from 0 to n-1 — not a sample, all of them — and takes the max valid-window-length at each one, you're guaranteed to have captured the true global maximum. You never had to explicitly check all O(n²) (l, r) pairs, because for each r, one number (the minimal l) dominates every other possible l for that same r — checking that one number is equivalent to having checked all of them.

One-sentence version to keep in your back pocket for interviews: "For every ending position, sliding window finds the longest valid substring ending there — and since every substring has some ending position, checking all endings is equivalent to checking all substrings, without the O(n²) cost."

