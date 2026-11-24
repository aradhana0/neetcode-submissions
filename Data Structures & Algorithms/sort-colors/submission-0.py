class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3

        for i in nums:
            colors[i] += 1
        
        i = 0
        for j in range(len(colors)):
            for _ in range(colors[j]):
                nums[i] = j
                i+=1
        
        return nums