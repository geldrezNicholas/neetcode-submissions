class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        maxA = 0

        while left < right:
            l = heights[left]
            r = heights[right]

            maxA = max(maxA, (right - left) * min(l, r))

            if l < r:
                left += 1
            else:
                right -= 1
        
        return maxA
