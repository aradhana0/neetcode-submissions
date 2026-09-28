class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        Rows, Cols = len(grid) - 1, len(grid[0]) - 1
        rotten = set()
        fresh = 0

        minutes = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
                    rotten.add((r, c))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
    
                neighbours = [(0,1), (0,-1), (-1,0), (1,0)]
                for dr, dc in neighbours:
                    if (
                        min(r + dr, c + dc) < 0 
                        or r + dr > Rows or c + dc > Cols
                        or (r + dr, c + dc) in rotten 
                        or grid[r + dr][c + dc] == 2
                        or grid[r + dr][c + dc] == 0
                    ):
                        continue

                    grid[r + dr][c + dc] = 2
                    queue.append((r+dr, c + dc))
                    rotten.add((r + dr, c + dc))
                    fresh -= 1
            minutes += 1
        
        if fresh > 0:
            return -1
        else:
            return minutes