class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            l = heights[left]
            r = heights[right]
            distance = right - left
            maxArea = max(min(l, r) * distance, maxArea)

            if l < r:
                left += 1
            else:
                right -= 1
        
        return maxArea
