class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        l,r = 0,len(nums)-1

        while l < r:
            m = l + (r-l)//2

            
            if nums[m] > nums[r]:
                l = m+1

            elif nums[m] == nums[r]:
                r = r - 1    

            else: # nums[m] < nums[r]:
                r = m
            

        return nums[l]            