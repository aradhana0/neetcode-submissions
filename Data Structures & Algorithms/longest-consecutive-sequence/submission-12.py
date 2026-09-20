class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLen = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                i = 1

                while num + i in numsSet:
                    i += 1
                    
                maxLen = max(i, maxLen)
             
        return maxLen