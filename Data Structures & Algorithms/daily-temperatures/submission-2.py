class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # minStk = [(temperatures[0],0)]
        l = len(temperatures)
        res = [0 for i in range(l)]
        i = 0
        stk = []

        while len(temperatures) > i:
            while len(stk) > 0 and stk[-1][0] < temperatures[i]:
                item = stk.pop()
                # print(item, i)
                res[item[1]] = i - item[1]

            stk.append((temperatures[i],i))
            # print(stk)
            i += 1

        return res
        