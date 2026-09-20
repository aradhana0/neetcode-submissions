class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSum = dict()

        for i, n in enumerate(nums):
            if n in targetSum:
                return [targetSum[n], i]
            targetSum[target - n] = i

      