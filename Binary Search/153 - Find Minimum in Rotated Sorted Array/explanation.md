The proof

The key fact: in a rotated sorted array, there’s at most one “drop” (where nums[i] > nums[i+1]), and the min sits right after it. If there’s no drop, the min is the first element.

The invariant is: the index of the minimum is always inside [l, r].

Initialization: [0, n-1] is the whole array, so it holds.
Maintenance, case nums[m] > nums[r]: Going from m to r, the values went down at some point, so the drop is somewhere in (m, r]. The min is after the drop, so it’s in [m+1, r]. And m can’t be the min, since something smaller (nums[r]) exists. So l = m + 1 keeps the invariant.
Maintenance, case nums[m] < nums[r]: There’s no drop between m and r, so nums[m..r] is increasing. The smallest thing in that stretch is nums[m], and everything after m is bigger. So the min is in [l, m]. m itself might be the min, which is why it’s r = m, not m - 1.
Termination: Since l < r, floor division gives m < r, strictly. So r = m always shrinks the range, l = m + 1 always shrinks it too, and the loop can’t run forever. It stops when l == r, a one-element range that must contain the min, so nums[r] (or nums[l], same thing) is the answer.

That m < r fact also answers the equality question. m and r are different indices, and the values are distinct, so nums[m] == nums[r] is impossible. The else branch is always the strict < case.

The interview version (about 30 seconds)

“I keep the invariant that the min is always in [l, r]. At each step I compare the middle to the right end. If nums[m] > nums[r], there’s a drop to the right of m, so the min is strictly right of m: l = m + 1. Otherwise m..r is sorted, so the min is at m or to its left: r = m, keeping m because it could be the answer. The range shrinks every iteration because m is always less than r, and when l == r that single element is the min. Each step halves the range, so it’s O(log n) time and O(1) space.”

Leading with the invariant is the move. It tells the interviewer you know why it’s correct, not just that it passes.

Classic traps for this pattern

r = m - 1 in the else branch throws away the min when m is the min.
while l <= r combined with r = m loops forever once l == r. The loop condition and the update rules have to agree.