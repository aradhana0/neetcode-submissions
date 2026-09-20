class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        L, R = 0, Rows - 1

        # find row
        while L <= R:
            mid = (L + R) // 2

            if target < matrix[mid][0]:
                R = mid - 1
            elif target > matrix[mid][-1]:
                L = mid + 1
            else:
                break
    
        if L > R:
            return False

        LRow = 0
        RRow = len(matrix[0]) - 1

        while LRow <= RRow:
            midRow = (LRow + RRow) // 2
            # print(LRow, RRow, midRow)
            if target < matrix[mid][midRow]:
                RRow = midRow - 1
            elif target > matrix[mid][midRow]:
                LRow = midRow + 1
            else:
                return True    
            # else: 
            #     return False
        return False