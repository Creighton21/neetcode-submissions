class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        result = float("inf")
        
        L = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                result = min(result, R - L + 1)
                total -= nums[L]
                L += 1

        return result if result != float("inf") else 0