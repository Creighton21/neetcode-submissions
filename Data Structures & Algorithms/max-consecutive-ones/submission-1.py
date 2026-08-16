class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0 

        current_count = 0
        for num in nums:
            if num == 0:
                current_count = 0
            else:
                current_count += 1
            
            if current_count > max_consecutive_ones:
                max_consecutive_ones = current_count

        return max_consecutive_ones