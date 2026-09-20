class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate = [i for i in range(1, max(piles) + 1)]
        minAns = float("inf")
        
        def calcTotalAtRate(k):
            total = 0

            for banana in piles:
                total = total + ((banana + k - 1) // k)

            return total

        L, R = 1, max(piles)

        while L <= R:
            mid = (L + R) // 2
            time = calcTotalAtRate(mid)
   
            if h < time:
                L = mid + 1
            elif h >= time:
                minAns = min(minAns, mid)
                R = mid - 1
            # else:
            #     return mid
        return minAns