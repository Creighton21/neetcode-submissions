class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for outer_index, outer_num in enumerate(nums):
            for inner_index, inner_num in enumerate(nums):
                if inner_index <= outer_index:
                    continue
                if inner_num + outer_num == target:
                    return [outer_index, inner_index]