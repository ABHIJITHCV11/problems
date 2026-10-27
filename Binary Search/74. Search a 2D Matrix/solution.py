class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        l,r = 0,len(matrix)-1

        while l <= r:
            m = l + (r-l) // 2

            if target >= matrix[m][0] and target <= matrix[m][-1]:
                print('here1')
                return self.binarySearch(matrix[m],target)

            elif target > matrix[m][-1]:
                l = m + 1
            else:
                r = m-1    

        return False

    def binarySearch(self, nums :list[int], target: int) -> bool:
        l,r = 0,len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if target > nums[m]:
                l = m + 1
            
            elif target == nums[m]: # early escape
                return True

            else:
                r = m   

        return nums[r] == target