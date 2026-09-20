class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [1] * length
        post = [1] * length
        res = []
        for i in range(1, length):
            pre[i] = pre[i - 1] * nums[i - 1] 
            post[i] = post[i - 1] * nums[-i]

        for i in range(0, length):
            res.append(pre[i] * post[-i - 1])
 
        return res

