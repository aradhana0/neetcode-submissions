class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        op = {
            '+','-',
            '*', '/'
        }

        for ch in tokens:
            if ch in op:
                res = 0
                b = stk.pop()
                a = stk.pop()
                if ch == '+':
                    res = a+b
                elif ch == '-':
                    res = a - b
                elif ch == '*':
                    res = a * b
                else: res = a/b
                stk.append(int(res))

            else:
                stk.append(int(ch))
        return int(stk[0])

        