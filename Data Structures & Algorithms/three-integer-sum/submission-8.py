class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        a = 0
        # b = 1
        # c = length - 1
        res = []

        nums = sorted(nums)
        for a  in range(length - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = length - 1
            while b < c:
                sum = (nums[b] + nums[c]) * -1
                if sum > nums[a]:
                    b += 1
                elif sum < nums[a]:
                    c -= 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1   
                    # Skip duplicate values for b
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1

                    # Skip duplicate values for c
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
            a += 1
        return res
                
            