class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        if n <= 1:
            return n

        i = 0
        while n > i:
            b, a = a + b, b
            i += 1

        return b