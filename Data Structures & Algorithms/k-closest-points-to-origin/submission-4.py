import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []

        heapq.heapify(res)

        for i in range(len(points)):
            distance = (points[i][0] ** 2) + (points[i][1] ** 2)
            dIndex = (distance, points[i])
            heapq.heappush(res, dIndex)

        return [heapq.heappop(res)[1] for i in range(k)]
