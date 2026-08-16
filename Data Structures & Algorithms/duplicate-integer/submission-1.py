class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res_set = set(nums)
        return len(res_set) != len(nums)