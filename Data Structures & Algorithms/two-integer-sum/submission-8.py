class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      numDict = {}
      i=0

      while i < len(nums):
        if nums[i] in numDict: 
            return [numDict[nums[i]],i]
        else: 
            numDict[target - nums[i]] = i
            i += 1

    #   return [] 

      