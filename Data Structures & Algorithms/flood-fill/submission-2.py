class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rLength = len(image)
        cLength = len(image[0])
        baseColor = image[sr][sc]
        def fill(r, c, visited):
            # edge case handling
            if min(r,c) < 0 or r == rLength or c == cLength or (r, c) in visited or image[r][c] != baseColor:
                return
            image[r][c] = color
            visited.add((r,c))

            fill(r+1, c, visited)
            fill(r-1, c, visited)
            fill(r, c+1, visited)
            fill(r, c-1, visited)

        fill(sr, sc, set())

        return image