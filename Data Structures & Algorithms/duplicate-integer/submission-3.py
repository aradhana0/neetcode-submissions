class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in nums:
            print(i)
            if i in map:
                return True
            else: 
                map[i] = 1 
        return False