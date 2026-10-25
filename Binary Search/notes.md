order of learning

1. 34 - Find First and Last Position of Element in Sorted Array
   Learn the templates first: first >= target and first > target (while l < r, r = len(nums), r = m).
   Everything after this is a variation on "shrink [l, r] while keeping the answer inside".

2. 153 - Find Minimum in Rotated Sorted Array
   First rotated problem. Compare nums[m] to nums[r], invariant "min index is in [l, r]".
   Learn why it's r = m (not m - 1) and why l < r pairs with it.

3. 33 - Search in Rotated Sorted Array
   153 + plain binary search. Find the min index, pick the piece using nums[-1], search that piece.

4. 154 - Find Minimum in Rotated Sorted Array II
   153 with duplicates. New case nums[m] == nums[r] -> r -= 1.
   Invariant changes from "min index" to "some copy of the min value". Worst case becomes O(n).

5. 81 - Search in Rotated Sorted Array II
   33 with duplicates = 33 + 154, plus one catch: we need the pivot INDEX, so before r -= 1
   check nums[r-1] > nums[r] (r is the pivot). The search step uses the 34 lower-bound template.

Dependency map
34 ----------------------------+
153 -> 33 ---------------------+-> 81
153 -> 154 --------------------+
