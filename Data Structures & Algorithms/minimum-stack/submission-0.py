class MinStack:
    def __init__(self):
        self.stk = list()

    def push(self, value: int) -> None:
        if len(self.stk) > 0:
            minVal = min(value, self.stk[-1][1])
        else: minVal = value
        self.stk.append((value, minVal))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
