The proof

It’s the same skeleton as 153, with one tweak: the invariant is now about the min value, not its index. 
With duplicates the min can appear at several indices, and we only need one copy to survive.

The invariant is: some copy of the minimum value is always inside [l, r].

The key fact still holds: the window is two non-decreasing pieces, and everything in the left piece is ≥ everything in the right piece. The min sits at the start of the right piece.

Case nums[m] > nums[r]: m and r can’t be in the same piece, since a piece never goes down. So m is in the left piece and r in the right, and the start of the right piece (the min) is in (m, r]. l = m + 1 keeps a copy. Same argument as 153.
Case nums[m] < nums[r]: m and r can’t be split across pieces, because left-piece values are ≥ right-piece values. So they’re in the same piece, nums[m..r] is non-decreasing, and nothing after m is smaller than nums[m]. The min is in [l, m], and r = m keeps it.
Case nums[m] == nums[r]: This is the new part. We can’t tell which side the min is on, but since m < r, the value nums[r] also lives at index m. Dropping index r loses no value from the range: if nums[r] was a copy of the min, its twin at m survives. So r = r - 1 keeps the invariant.
Termination: Every branch shrinks the range by at least one (l moves right, or r moves left, since m < r). It ends at l == r, and that single element must be the min.

The interview version

“Same idea as the distinct case: compare the middle to the right end, keeping the invariant that the min value is in [l, r]. If nums[m] > nums[r], the min is strictly right of m. If nums[m] < nums[r], m..r is sorted, so the min is at m or left of it. The new case is equality: I can’t tell which side the min is on, but nums[r] has a copy at m, so dropping r is safe, and I shrink by one. That keeps correctness but makes the worst case O(n), for example when most elements are equal. And that’s unavoidable: in something like [1,1,1,0,1,1], any algorithm has to look at every position, because the 0 could be hiding anywhere.”

That last sentence is a strong closer.