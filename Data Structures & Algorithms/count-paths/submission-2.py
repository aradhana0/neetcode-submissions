class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def helper(r, c, cache = dict()):
            if r >= m or c >= n:
                return 0

            if (r, c) in cache:
                return cache[(r,c)]

            if r == m - 1 and c == n - 1:
                return 1

            cache[(r,c)] = helper(r + 1, c) + helper(r, c+1)
            return cache[(r,c)]

        return helper(0, 0)