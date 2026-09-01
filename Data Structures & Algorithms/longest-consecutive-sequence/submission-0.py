class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()

        result = 1
        current_seq = 1
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) == 1:
                current_seq += 1
            elif (nums[i] - nums[i-1]) == 0:
                continue
            else:
                result = max(result, current_seq)
                current_seq = 1

        return max(result, current_seq)