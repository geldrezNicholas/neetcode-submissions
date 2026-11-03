class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        gridLength = len(grid)

        if grid[0][0] == 1 or grid[gridLength - 1][gridLength - 1] == 1:
            return -1

        q = deque([(0, 0, 1)])
        visit = set([(0, 0)])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()
            if min(r, c) < 0 or max(r, c) == gridLength or grid[r][c] == 1:
                continue
            
            if r == gridLength - 1 and c == gridLength - 1:
                return length
            
            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        
        return -1
