class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right: 
            l = heights[left]
            r = heights[right]

            width = right - left
            height = min(l, r)

            maxArea = max(maxArea, width * height)

            if l > r:
                right -= 1
            else:
                left += 1
        
        return maxArea
