class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        cache = [[-1] * n2 for i in range(n1)]

        def dfs(str1_idx, str2_idx):
            if str1_idx >= n1 or str2_idx >= n2:
                return 0
            
            if cache[str1_idx][str2_idx] != -1:
                return cache[str1_idx][str2_idx]

            if text1[str1_idx] == text2[str2_idx]:
                cache[str1_idx][str2_idx] = 1 + dfs(str1_idx + 1, str2_idx + 1)
            else:
                cache[str1_idx][str2_idx] = max(dfs(str1_idx + 1, str2_idx), dfs(str1_idx, str2_idx + 1))

            return cache[str1_idx][str2_idx]

        return dfs(0, 0)