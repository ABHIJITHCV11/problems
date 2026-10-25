class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        def first(nums, target):
            # [5,7,7,8,8,10] 8
            # [T,T,T,F,F,F]

            l, r = 0, len(nums) - 1

            while l < r:
                m = l + (r - l) // 2
                if target > nums[m]: # first occurance of the target is strictly to the right
                    l = m + 1       
                elif target < nums[m]: # this doesnt make much difference can ignore
                    r = m -1 
                else:
                    r = m # nums[m] might be the first occurance             
            if not nums or nums[l] != target:
                return -1               
            else:
                return l                  # first occurrence

        def last(nums, target):
            # [5,7,7,8,8,10] 8
            # [T,T,T,T,T,F]       go-right condition: target >= nums[i]
            # first F = one past the last 8 → answer is l - 1
    
            # r = len(nums), not n - 1: if target is the LAST element,
            # every index is T, so the first F is "index n" (past the end).

            l, r = 0, len(nums)

            while l < r:
                m = l + (r - l) // 2
                if target >= nums[m]:   # T → last occurrence is at m or to the right
                    l = m + 1
                else:                   # F → m might be the first F, keep it
                    r = m

            return l - 1                # last occurrence

        l = first(nums, target)
        if l == -1:
            return [-1, -1]               # target not in nums → skip the second search
        else:
            return [l, last(nums, target)]

        # Python built-ins do the same thing:
        #   first → bisect.bisect_left(nums, target) 
        # : lands on the first occurrence, no adjustment needed.

        #   last  → bisect.bisect_right(nums, target) - 1
        # : lands one past the last occurrence, so subtract 1.