class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaList = {}
        for c in strs:
            cnt = str(Counter("".join(sorted(c))))
            if cnt in anaList:
                anaList[cnt].append(c)
            else:
                anaList[cnt] = [c]
        # print(anaList)
        return list(anaList.values())

        
