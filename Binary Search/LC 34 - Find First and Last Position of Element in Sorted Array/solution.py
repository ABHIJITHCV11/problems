class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def first_ge(target):
            # first index where nums[i] >= target
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l

        def first_gt(target):
            # first index where nums[i] > target
            l, r = 0, len(nums)
            while l < r:
                m = l + (r - l) // 2
                if nums[m] > target:
                    r = m
                else:
                    l = m + 1
            return l

        start = first_ge(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = first_gt(target) - 1
        return [start, end]