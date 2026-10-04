class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        answer = 0
        def isSubsequence(s1):
            i = 0

            for s in text2:
                if i < len(s1) and s == s1[i]:
                    i += 1

            
            return i == len(s1)


        def generate(i, current, cache = {}):
            nonlocal answer

            if (i, current) in cache:
                return cache[(i, current)]

            if i == len(text1):
                if isSubsequence(current):
                    return len(current)
                return 0

            cache[(i + 1,current)] = generate(i + 1, current, cache)
            cache[(i + 1,current + text1[i])] = generate(i + 1, current + text1[i], cache)

            return max(cache[(i + 1,current)], cache[(i + 1,current + text1[i])])

        return generate(0, "")