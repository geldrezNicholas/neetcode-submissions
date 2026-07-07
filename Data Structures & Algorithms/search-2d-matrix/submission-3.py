class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L1, R1 = 0, len(matrix)-1

        while L1 <= R1:
            M1 = (L1+R1)//2
            if target < matrix[M1][0]:
                R1 = M1 - 1
            elif target > matrix[M1][-1]:
                L1 = M1 + 1

            else:
                L2, R2 = 0, len(matrix[M1])-1
                while L2 <= R2:
                    M2 = (L2+R2)//2
                    if target < matrix[M1][M2]:
                        R2 = M2 - 1
                    elif target > matrix[M1][M2]:
                        L2 = M2 + 1
                    else:
                        return True
                return False
        return False