class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def bt(i): 
            if i == len(nums):
                result.append(subset.copy())
                return;

            # include in subset
            subset.append(nums[i])
            bt(i+1)

            #exclude from subset
            subset.pop()
            bt(i+1)
        

        bt(0)

        return result