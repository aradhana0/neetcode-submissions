class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        
        if lenS != lenT: return False

        mapS = {}
        mapT = {}

        for i in t:
            mapT[i] = mapT.get(i, 0) + 1
      
        for c in s:
            if c in mapT:
                mapT[c] = mapT[c] - 1 
            else:
                return False

        for i in mapT:
            if mapT[i] > 0:
                return False

        return True