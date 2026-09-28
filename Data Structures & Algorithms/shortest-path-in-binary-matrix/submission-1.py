class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        visited = set()

        if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
            return -1

        queue.append((0,0))
        visited.add((0,0))

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                if r == ROWS and c == COLS:
                    return length

                neighbours = [(0,1), (-1,1), (1,-1),(1,1),(-1,-1), (0,-1), (-1,0), (1,0)]

                for dr, dc in neighbours:
                    if (
                        min(r + dr, c + dc) < 0 or r + dr > ROWS or c + dc > COLS 
                        or (r + dr, c + dc) in visited or grid[r+dr][c+dc] == 1
                    ):
                        continue

                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

            length += 1

        return -1