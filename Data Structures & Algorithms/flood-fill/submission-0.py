class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, sr, sc, color, start_color, visit):
            ROWS, COLS = len(image), len(image[0])

            # Base Cases
            # If we are out of bounds to the left or top
            if min(sr,sc) < 0:
                return
            # If we are out of bounds to the right or bottom
            if sr >= ROWS or sc >= COLS:
                return
            # If visited don't visit again
            if (sr,sc) in visit:
                return
            # If the node is not the start_color
            if image[sr][sc] != start_color:
                return

            image[sr][sc] = color

            visit.add((sr,sc))

            dfs(image, sr+1, sc, color, start_color, visit)
            dfs(image, sr-1, sc, color, start_color, visit)
            dfs(image, sr, sc+1, color, start_color, visit)
            dfs(image, sr, sc-1, color, start_color, visit)
            
        dfs(image, sr, sc, color, image[sr][sc], set())

        return image
