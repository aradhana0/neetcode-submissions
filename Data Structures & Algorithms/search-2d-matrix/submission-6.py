class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1

        if rows == 0 and cols == 0:
            if matrix[0][0] == target:
                return True
            return False

        l = 0
        r = rows

        while r > l:
            mid = (l + r) // 2

            if matrix[mid][cols] == target:
                return True

            if matrix[mid][cols] > target:
                r = mid
            else:
                l = mid + 1

        s = 0
        e = cols

        while s < e:
            mid = (s + e) // 2

            if matrix[l][mid] == target:
                    return True

            if matrix[l][mid] > target:
                e = mid
            else:
                s = mid + 1

        return matrix[l][s] == target