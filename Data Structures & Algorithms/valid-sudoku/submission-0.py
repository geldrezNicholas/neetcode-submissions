from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            rows = set()
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                else:
                    if num in rows or num in cols[col] or num in squares[(row // 3, col // 3)]:
                        return False
                    else:
                        rows.add(num)
                        cols[col].add(num)
                        squares[(row // 3, col // 3)].add(num)

        return True