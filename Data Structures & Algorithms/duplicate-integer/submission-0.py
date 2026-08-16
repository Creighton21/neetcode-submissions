class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()

        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = num

        return False