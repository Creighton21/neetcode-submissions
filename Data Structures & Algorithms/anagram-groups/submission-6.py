class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            counts =[0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)

            groups.setdefault(key, []).append(s)

        return list(groups.values())