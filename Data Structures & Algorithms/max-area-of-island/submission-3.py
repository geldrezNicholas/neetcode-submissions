class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):

            if r == ROWS or c == COLS or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            

            counter = 1
            grid[r][c] = 0
            counter += dfs(r + 1, c)
            counter += dfs(r - 1, c)
            counter += dfs(r, c + 1)
            counter += dfs(r, c - 1)

            return counter
        
        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        
        return maxArea
