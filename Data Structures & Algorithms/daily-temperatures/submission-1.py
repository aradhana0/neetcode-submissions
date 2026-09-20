class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        i = 0
        j = i + 1
        temp_count = len(temperatures)

        if temp_count < 2:
            return [0]
        while i < temp_count:
            if j >= temp_count:
                result.append(0)
                i = i+1
                j = i+1
            elif temperatures[j] > temperatures[i]:
                result.append(j - i)
                i = i + 1
                j = i + 1
            else:
                j = j + 1

        return result
        