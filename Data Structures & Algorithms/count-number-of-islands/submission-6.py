class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rLength = len(grid)
        cLength = len(grid[0])
        islandCount = 0

        def visitIsland(r, c):
            if min(r,c) < 0 or r == rLength or c == cLength or grid[r][c] == "0" or (r,c) in visited:
                return

            visited.add((r,c))

            visitIsland(r + 1, c)
            visitIsland(r - 1, c)
            visitIsland(r, c + 1)
            visitIsland(r, c - 1)
            
        for r in range(rLength):
            for c in range(cLength):
                if (r,c) not in visited and grid[r][c] == "1":
                    islandCount += 1
                    visitIsland(r, c)

        return islandCount