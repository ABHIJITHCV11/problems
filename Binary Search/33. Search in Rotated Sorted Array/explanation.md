The idea

Don't fight the rotation, undo it. A rotated sorted array is two sorted pieces glued together, and the min is where the second piece starts.
So: find the min index with the 153 template, decide which piece the target can be in, then run a plain binary search on that piece.

The proof

Let p be the index of the min (from findMin, which is exactly 153, so its correctness carries over).
Then nums[0..p-1] is the left piece, nums[p..n-1] is the right piece, both sorted, and every left-piece value is bigger than every right-piece value.
nums[-1] is the largest value in the right piece.

Case target > nums[-1]: target is bigger than everything in the right piece, so it can only be in the left piece. Search [0, p-1].
Case target <= nums[-1]: every left-piece value is > nums[-1] >= target, so target can't be in the left piece. Search [p, n-1].
Either way we search a sorted range that contains target if target exists at all, so standard binary search finishes the job.

Edge case: no rotation (p = 0). The left piece is empty. If target > nums[-1], it's bigger than the whole array, binarySearch(0, -1) never enters the loop and returns -1. Correct.

Why nums[-1] and not nums[0]? Both work, but nums[-1] splits cleanly: "> nums[-1]" means left piece, otherwise right piece, and the empty-left-piece case falls out for free.

Cost: two binary searches, O(log n) time, O(1) space.

The interview version

"A rotated sorted array is two sorted halves, and the boundary is the minimum. I find the min index with the usual compare-middle-to-right binary search. Then I compare the target to the last element: if it's bigger, it can only be in the left half, since every right-half value is at most nums[-1]; otherwise it can only be in the right half, since every left-half value is bigger than nums[-1]. Then a normal binary search on that half. Two log n passes, so O(log n) time, O(1) space."

If they ask for one pass: compare nums[l] to nums[m] to see which half of [l, r] is sorted, check if target falls inside that sorted half's range, and go there, otherwise go to the other half. Same complexity, more conditions to get wrong. The two-pass version is easier to prove out loud.

Classic traps for this pattern

Using >= nums[0] to pick the left piece: fine for rotated arrays, but if there's no rotation, everything is >= nums[0] and you search an empty left piece. Pick the split that handles p = 0.
Mixing templates: findMin uses while l < r with r = m; the exact-match search uses while l <= r with r = m - 1. Swapping either loop condition breaks it (infinite loop or missed element).
This only works because values are distinct. With duplicates, findMin can't always tell which side to go, see 81.
