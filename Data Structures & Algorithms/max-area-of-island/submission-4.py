class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rLength = len(grid)
        cLength = len(grid[0])
        maxArea = 0
        area = 0

        def visitIsland(r, c):
            nonlocal area, visited, maxArea
            if min(r,c) < 0 or r == rLength or c == cLength or grid[r][c] == 0 or (r,c) in visited:
                return
            
            visited.add((r,c))
            if grid[r][c] == 1:
                area += 1
           
            visitIsland(r + 1, c)
            visitIsland(r - 1, c)
            visitIsland(r, c + 1)
            visitIsland(r, c - 1)
            
            maxArea = max(area, maxArea)
        
        for r in range(rLength):
            for c in range(cLength):
                if (r,c) not in visited and grid[r][c] == 1:
                    # maxArea = max(area, maxArea)
                    area = 0
                    # print("area, maxArea")
                visitIsland(r, c)

        return maxArea