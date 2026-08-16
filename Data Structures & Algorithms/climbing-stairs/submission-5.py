class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(steps):
            if steps == 0:
                return 1
            if steps < 0:
                return 0
            if steps in memo:
                return memo[steps]

            count = 0
            count += dfs(steps-1)
            count += dfs(steps-2)
            memo[steps] = count

            return count

        return dfs(n)