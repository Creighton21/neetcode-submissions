class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for num in num_set:
            if num - 1 in num_set:
                continue # It belongs to a parent sequence (not the smallest in the sequence)

            length = 1
            while num + length in num_set: # Build our sequence length
                length += 1

            result = max(result, length)

        return result