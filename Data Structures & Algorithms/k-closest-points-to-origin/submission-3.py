import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []

        for p in points:
            distance = math.sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(heap, (distance, p))
            
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result