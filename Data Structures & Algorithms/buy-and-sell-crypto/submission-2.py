class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxP = 0
        minP = 101
        for p in prices:
            if minP >= p:
                minP = p
                maxP = 0
            elif maxP <= p:
                maxP = p
            if maxP != 0:
                profit = max(maxP - minP, profit)


        return profit