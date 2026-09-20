class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # lenS = len(s)
        # lenT = len(t)
        
        # if lenS != lenT: return False

        # mapS = {}
        # mapT = {}

        # for i in s:
        #     mapS[i] = mapS.get(i, 0) + 1
      
        # for i in t:
        #     mapT[i] = mapT.get(i, 0) + 1
      
        # return mapS == mapT


        