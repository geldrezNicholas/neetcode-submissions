class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = matrix[0]
        for e in range(1, len(matrix)):
            nums.extend(matrix[e])
        print(nums)
        
        if target < nums[0] or target > nums[-1]:
            return False

        L, R = 0, len(nums)-1

        while L <= R:
            M = (L+R)//2

            if nums[M] > target:
                R = M-1
            elif nums[M] < target:
                L = M+1
            else:
                return True
        return False