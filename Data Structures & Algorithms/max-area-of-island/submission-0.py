class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfsCount(r, c):

            if r == ROWS or c == COLS or min(r, c) < 0 or grid[r][c] == 0:
                return 0
            
            count = 1
            grid[r][c] = 0

            count += dfsCount(r + 1, c)
            count += dfsCount(r - 1, c)
            count += dfsCount(r, c + 1)
            count += dfsCount(r, c - 1)

            return count


            # if out of bounds or 0, return 0 

            # if 1 add one but also call on rest of area and set to 0

        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    currArea = dfsCount(row, col)
                    if currArea > maxArea:
                        maxArea = currArea

        return maxArea

