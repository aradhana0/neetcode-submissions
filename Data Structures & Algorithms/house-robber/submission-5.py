class Solution:
    def rob(self, nums: List[int]) -> int:
        result = []
        if len(nums) == 1:
            return nums[0]
        rob = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            rob.append(max(rob[i-1], rob[i - 2] + nums[i]))

        return rob[-1] 

        