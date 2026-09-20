class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # step 1 - add the list to hash set
        # step 2 - create a dict variable to store the sequence/length of the sequence + keep track of max length
        # step 3 - iterate the list
        # step 4 - check if the list item is the root, if yes: build the sequence in the dict for the list item and keep deleting the items added to the sequence from the hash set
        # step 5 - if not, move to the next list item

        numsSet = set(nums)
        conSeqDict = {}
        maxLen = 0

        # if len(numsSet) <= 1:
        #     return len(numsSet)
        for num in numsSet:
            if num - 1 not in numsSet:
                i = 1
                conSeqDict[num] = []

                while num + i in numsSet:
                    conSeqDict[num].append(num + i)
                    i += 1
                    
                maxLen = max(i, maxLen)
             
        return maxLen