class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        length = 1
        obj = {s[0]}
        i = 0
        j = 1
        maxLength = 1

        while j < len(s):
            if s[j] not in obj:
                obj.add(s[j])
                j += 1
                length += 1
            else:
                obj.remove(s[i])
                i += 1
                # j += 1
                length -= 1
            # print(obj)
            maxLength = max(length, maxLength)

        return maxLength