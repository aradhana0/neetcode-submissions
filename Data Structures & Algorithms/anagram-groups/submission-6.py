class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()

        for s in strs:
            sorted_s = tuple(sorted(s))
            
            if sorted_s in anagramDict:
                anagramDict[sorted_s].append(s)
            else:
                anagramDict[sorted_s] = [s]

        return list(anagramDict.values())