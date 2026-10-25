class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Search range: all possible ANSWERS (0..n)
        # n is a valid answer: it means "insert after everything"
        l, r = 0, len(nums)

        while l < r:
            m = l + (r - l) // 2          # floor mid, so m < r always,
                                          # which means nums[m] never goes out of bounds

            if target > nums[m]:
                l = m + 1                 # condition fails: answer is strictly right of m
            else:                         # nums[m] >= target: condition holds
                r = m                     # answer is m or left of it, keep m

        # Loop ends with l == r: the first index where nums[i] >= target
        # (or n if no such index exists)
        return l