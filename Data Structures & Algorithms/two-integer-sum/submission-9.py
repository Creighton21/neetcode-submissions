class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key, value in enumerate(nums):
            # Get the difference or the complement of our current num
            difference = target - value
            # Have we already seen the complement
            if difference in seen:
                return [seen[difference], key]
            seen[value] = key
