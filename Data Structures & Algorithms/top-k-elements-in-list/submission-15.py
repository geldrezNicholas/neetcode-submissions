from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k == 0:
            return []

        freq = [[] for x in range(len(nums) + 1)]
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1
        
        for num, count in counter.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if k == len(res):
                    return res
        
        return res


