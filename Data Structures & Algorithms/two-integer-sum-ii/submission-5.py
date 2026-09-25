class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            l = numbers[left]
            r = numbers[right]
            if l + r == target:
                return [left + 1, right + 1]
            elif l + r < target:
                left += 1
            elif l + r > target:
                right -= 1
            
        
        return []

            