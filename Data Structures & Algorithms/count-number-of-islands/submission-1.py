class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r,c) < 0: # out of bounds
                return
            if r >= ROWS or c >= COLS: # out of bounds
                return
            if (r,c) in visited: # already seen it
                return
            if grid[r][c] == "0": # not on land
                return
            # What are the conditions now?
            # I want to visit every node 

            # What to do to process the current node?
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    count += 1
        return count