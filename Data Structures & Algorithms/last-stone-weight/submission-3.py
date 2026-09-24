class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -1 * s)

        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)

            if s1 != s2:
                heapq.heappush(heap, -1 * abs(s1 - s2))

        return heap[0] * -1 if len(heap) > 0 else 0