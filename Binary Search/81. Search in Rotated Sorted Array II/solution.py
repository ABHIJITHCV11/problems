class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        pivot = self.findPivot(nums)
        if target > nums[-1]:
            return self.binarySearch(nums, 0, pivot - 1, target)
        return self.binarySearch(nums, pivot, len(nums) - 1, target)

    def findPivot(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                if nums[r - 1] > nums[r]:   # r is the rotation point
                    return r
                r -= 1
        return l

    def binarySearch(self, nums: list[int], l: int, r: int, target: int) -> bool:
        # if l > r:
        #     return False
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return nums[l] == target