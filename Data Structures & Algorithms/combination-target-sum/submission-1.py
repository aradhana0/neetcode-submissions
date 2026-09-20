class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []
        def helper(idx, total):
            # success
            if total == target:
                result.append(combinations.copy())
                return
            # invalid path
            if idx >= len(nums) or total > target:
                return

            combinations.append(nums[idx])
            helper(idx, total + nums[idx])

            combinations.pop()
            helper(idx + 1, total)
           
        
        helper(0,  0)

        return result
