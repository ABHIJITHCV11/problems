class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min_index = self.findMin(nums)

        # search left side
        if target > nums[-1]:
            return self.binarySearch(0,min_index-1,target,nums)
        else:
            return self.binarySearch(min_index,len(nums)-1,target,nums)    

    
    def binarySearch(slef,l,r,target,nums) -> int:    
        while l <= r:
            m = l + (r-l)//2
            if target > nums[m]:
                l = m +1
            elif target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m    
        return -1

    def findMin(slef,nums) -> int:    
        l,r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]: 
                r = m
        print(nums[r],r)        
        return r