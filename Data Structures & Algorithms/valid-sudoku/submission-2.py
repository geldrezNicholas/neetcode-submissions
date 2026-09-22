from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            rows= set()
            for col in range(9):
                item = board[row][col]
                if item == '.':
                    continue
                else:
                    if item in rows or item in cols[col] or item in squares[(row // 3, col // 3)]:
                        return False
                    else:
                        rows.add(item)
                        cols[col].add(item)
                        squares[(row // 3, col // 3)].add(item)

            
        return True
                