class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Loop over nums
            # keep track of number of times each number seen
            # if count is greater than k_most_common counts or the len
            # of k_most_common is less than k then add or replace it.
        
        k_most_common = []
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] = counts[num] + 1

            if num in k_most_common:
                continue
            
            k_most_common_counts = [counts[i] for i in k_most_common]

            if len(k_most_common) < k:
                k_most_common.append(num)

            if any(counts[num] > x for x in k_most_common_counts):
                index_to_replace = k_most_common_counts.index(min(k_most_common_counts))
                k_most_common[index_to_replace] = num
                

        return k_most_common