class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaList = {}

        for i in range(len(strs)):
            sortedItem = "".join(sorted(strs[i]))
            if sortedItem in anaList:
                anaList[sortedItem].append(strs[i])
            else: 
                anaList[sortedItem] = [strs[i]]

        return list(anaList.values())
        
