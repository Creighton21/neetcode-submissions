class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        
        def dfs(image, sr, sc):
            # Base Cases
            # If we are out of bounds to the left or top
            if min(sr,sc) < 0:
                return
            # If we are out of bounds to the right or bottom
            if sr >= ROWS or sc >= COLS:
                return
            # If the node is not the start_color
            if image[sr][sc] != start_color:
                return

            image[sr][sc] = color

            dfs(image, sr+1, sc)
            dfs(image, sr-1, sc)
            dfs(image, sr, sc+1)
            dfs(image, sr, sc-1)
            
        dfs(image, sr, sc)

        return image
