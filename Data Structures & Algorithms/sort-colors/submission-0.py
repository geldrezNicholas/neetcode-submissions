class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for e in range(len(nums)):
            colors[nums[e]] += 1
        n = 0
        for i in range(len(colors)):
            for j in range(colors[i]):
                nums[n] = i 
                n += 1