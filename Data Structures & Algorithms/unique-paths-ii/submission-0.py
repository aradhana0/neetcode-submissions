class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) 
        n = len(obstacleGrid[0])
        def helper(r, c, cache = dict()):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0

            if (r, c) in cache:
                return cache[(r,c)]

            if r == m - 1 and c == n - 1:
                return 1

            cache[(r,c)] = helper(r + 1, c) + helper(r, c+1)
            return cache[(r,c)]

        return helper(0, 0)