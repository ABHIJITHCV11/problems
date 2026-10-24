class Solution:
    def findMin(self, nums: list[int]) -> int:

        l,r = 0,len(nums)-1

        while l < r:
            m = l + (r-l)//2
            
            if nums[m] > nums[r]:
                l = m + 1
  
            elif nums[m] < nums[r]: # what if nums[m] == nums[r] | this wont happen in 153 
                r = m
        
        return nums[r]