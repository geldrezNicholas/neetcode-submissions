class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r == ROWS or c == COLS or min(r, c) < 0 or grid[r][c] == "0":
                return 0
            
            counter = 1
            grid[r][c] = "0"

            counter += dfs(r + 1, c)
            counter += dfs(r - 1, c)
            counter += dfs(r, c + 1)
            counter += dfs(r, c - 1)

            return counter
        
        totalIslands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    totalIslands += 1
                    dfs(row, col)
            
        return totalIslands