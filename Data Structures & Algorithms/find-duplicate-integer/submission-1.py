class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0 for _ in range(10001)]

        for num in nums:
            if arr[num] > 0:
                return num
            arr[num] += 1


        # hashSet = set()
        # for num in nums:
        #     if num in hashSet:
        #         return num
        #     hashSet.add(num)

         