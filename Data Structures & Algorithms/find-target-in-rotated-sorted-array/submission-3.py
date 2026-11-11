class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            
            l, r, m = nums[left], nums[right], nums[mid]

            if m == target:
                return mid
            elif l <= m:
                if l <= target < m:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if m < target <= r:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

