class Solution:
    def searchList(self, nums: list, target: int) -> int:
        l,r = 0, (len(nums) - 1)

        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            index = self.searchList(nums, target)
            if index != -1:
                return True
        return False