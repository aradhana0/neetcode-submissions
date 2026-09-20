class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hsr, hsc, hsSubBox = set(), set(), set()
        r = 0 
        c = 0
        
        def isValid(r, c, hashSet):
            if board[r][c] in hashSet or (board[r][c] != "." and ("1" > board[r][c] or board[r][c] > "9")):
                return False
            return True

        def checkRowValidity():
            for r in range(0,9):
                hsr = set()
                for c in range(0,9):
                    if not isValid(r, c, hsr):
                        return False
                    if board[r][c] != ".":
                        hsr.add(board[r][c])
            return True

        def checkColValidity():
            for c in range(0,9):
                hsc = set()
                for r in range(0,9):
                    if not isValid(r, c, hsc):
                        return False
                    if board[r][c] != ".":
                        hsc.add(board[r][c])
            return True

        def checkSubBoxValidity():
            for rBoundary in range(0, 9, 3):
                for cBoundary in range(0, 9, 3):
                    hsSubBox = set()
                    for r in range(rBoundary, rBoundary + 3):
                        for c in range(cBoundary, cBoundary + 3):                
                            if not isValid(r, c, hsSubBox):
                                return False
                            if board[r][c] != ".":
                                hsSubBox.add(board[r][c])
            return True

        
                    
        return checkRowValidity() and checkColValidity() and checkSubBoxValidity()

      