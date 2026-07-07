class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        if target > nums[R] or target < nums[0]:
            return -1

        while L <= R:
            M = (L+R)//2
            if target < nums[M]:
                R = M-1
            elif target > nums[M]:
                L = M+1
            else:
                return M
        return -1