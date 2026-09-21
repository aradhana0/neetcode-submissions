class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []
        result = []

        def bt(o, c):
            # success
            if len(combination) == n * 2:
                result.append("".join(combination))
                return

            if o < n:
                combination.append("(")
                bt(o + 1, c)
                combination.pop()
            if c < o:
                combination.append(")")
                bt(o, c+1)
                combination.pop()
            
            

        bt(0, 0)

        return result