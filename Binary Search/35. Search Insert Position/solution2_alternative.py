class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Search range: valid indices only (0..n-1)
        # Note: the answer n ("insert after everything") is NOT in this range
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2          # floor mid, so m < r always

            if target > nums[m]:
                l = m + 1                 # m is too small, answer is strictly right of m
            elif target < nums[m]:
                r = m                     # m could be the insert position, keep it
            else:
                return m                  # exact match found

        # Loop ends with l == r: the first index where nums[l] >= target,
        # OR the last index (n-1) if every element is smaller than target.
        # Fix-up: if target is bigger than nums[l], insert after it.
        if target > nums[l]:
            return l + 1
        return l