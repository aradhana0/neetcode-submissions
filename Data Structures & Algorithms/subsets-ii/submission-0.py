class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # visited = [False for i in range(len(nums) + 1)]
        subset = []
        result = []

        def bt(idx):
            if len(nums) <= idx: 
                result.append(subset.copy())
                return
            else:
                subset.append(nums[idx])
                bt(idx+1)
                subset.pop()
                while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                    idx += 1
                
                bt(idx + 1)

        bt(0)

        return result
