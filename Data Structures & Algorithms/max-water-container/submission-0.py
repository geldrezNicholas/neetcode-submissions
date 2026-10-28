class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1

        maxArea = 0
        while left < right:
            l = heights[left]
            r = heights[right]
            distance = (right + 1) - (left + 1)

            smallest = min(l, r)
            newArea = smallest * distance
            maxArea = max(maxArea, newArea)

            if l < r:
                left += 1
            else:
                right -= 1

        
        return maxArea