class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # Is this true, this would be a question I would ask
        # I assume it is for now
        if grid[0][0] == 1:
            return -1
        if grid[ROWS-1][COLS-1] == 1:
            return -1

        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))


        length = 1
        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                r,c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length

                directions = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1, 1], [1,-1], [1,1]]
                # what are the other 4 directions?
                """
                at 1,1
                    000
                    000
                    000
                """
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Are we out of bounds?
                    if (nr < 0 or nc < 0 or 
                        nr == ROWS or nc == COLS or
                        (nr, nc) in visit or
                        grid[nr][nc] == 1):
                        continue
                    
                    visit.add((nr, nc))
                    queue.append((nr, nc))
            length += 1
        return -1
