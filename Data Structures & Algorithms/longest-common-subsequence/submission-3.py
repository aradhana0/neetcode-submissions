class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        grid = [[0] * (n + 1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    grid[i+1][j+1] = 1 + grid[i][j]
                else:
                    grid[i+1][j+1] = max(grid[i][j+1], grid[i+1][j])

        return grid[-1][-1]