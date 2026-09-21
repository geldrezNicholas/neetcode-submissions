from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k == 0:
            return []
        
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) == k:
                    return res
                res.append(j)
    
        
        return res

        
            

