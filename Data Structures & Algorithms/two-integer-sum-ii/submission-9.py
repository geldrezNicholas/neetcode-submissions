class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            l = numbers[left]
            r = numbers[right]

            if r + l == target:
                return [left + 1, right + 1]
            elif r + l > target:
                right -= 1
            else:
                left += 1
            
        return []

            