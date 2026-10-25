The idea

Same plan as 33: find the rotation point, pick the piece the target belongs to, binary search that piece.
The difference is duplicates, which hit findPivot exactly the way they hit 154. And here we need the actual rotation index, not just the min value, which adds one extra check.

The proof

Let p be the rotation point: the index where the drop happens (nums[p-1] > nums[p]). If there's no drop, the array is just non-decreasing and p = 0.

findPivot invariant: p is always inside [l, r].

Case nums[m] > nums[r]: a piece never goes down, so m is in the left piece and r in the right. p is in (m, r], so l = m + 1. Same as 153/154.
Case nums[m] < nums[r]: left-piece values are >= right-piece values, so m and r are in the same piece and p is not in (m, r]. p is in [l, m], so r = m.
Case nums[m] == nums[r]: can't tell the side. In 154 we just did r -= 1, because we only needed some copy of the min VALUE to survive. Here we need the INDEX p, and r -= 1 loses it if r == p.
  r == p means nums[r-1] > nums[r] (that's the definition of the drop), so check that first and return r.
  Otherwise r != p, so p is in [l, r-1] and r -= 1 is safe.
  r - 1 is always valid because l < r means r >= 1.
No drop at all: nums[m] > nums[r] never happens, so l stays 0 and we return 0. Correct.
Termination: every branch shrinks [l, r] (or returns), ends at l == r == p.

Why the extra check matters, concrete example: [1, 1, 1, 2, 1], target = 2.
Without it: r=4, m=2, equal, r=3. m=1, 1 < 2, r=1. m=0, equal, r=0. Returns 0, but the real pivot is 4.
Then 2 > nums[-1] sends us to search [0, -1], and we return False. Wrong.
With it: at r=4, nums[3]=2 > nums[4]=1, so return 4. Search [0, 3], find 2.

The search step: same split as 33. target > nums[-1] means left piece [0, p-1], else right piece [p, n-1].
Each piece is sorted, so binarySearch finds the first index with nums[i] >= target (lower bound, the 34 template) and checks if it's equal.
If the left piece is empty (p = 0), binarySearch(0, -1) skips the loop and checks nums[0] == target. That's False, because target > nums[-1] >= nums[0] when there's no rotation. Correct, if a bit accidental.

Cost: worst case O(n), e.g. [1,1,1,1,0,1,1] makes findPivot shrink one step at a time. Best case O(log n). Space O(1).

The interview version

"Same as the distinct version: find the rotation point, then binary search the half that can contain the target. Duplicates break the pivot search when nums[m] == nums[r], because I can't tell which side the drop is on. I shrink r by one, which is safe unless r itself is the rotation point, and I can check that directly: if nums[r-1] > nums[r], r is the pivot, return it. Then it's one binary search on the correct half. Worst case is O(n), and that's unavoidable: with an array of all 1s and a single 2 hidden somewhere, any algorithm has to look at every position to find it."

Classic traps for this pattern

Copying 154's findMin as-is. It's correct for the min value but can return the wrong index, see the example above.
Returning l without the r - 1 guard and "testing" only on arrays where the duplicates happen to sit in one piece. Test cases like [1,1,1,2,1] and [1,0,1,1,1].
Claiming O(log n). With duplicates it's O(n) worst case, say so before they ask.
