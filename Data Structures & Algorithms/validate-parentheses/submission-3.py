class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dict = { 
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in s:
            if ch not in dict:
                stk.append(ch)
            else:
                if len(stk) == 0 or stk[len(stk) - 1] not in dict[ch]:
                    return False
                else:
                    stk.pop()
        return len(stk) == 0