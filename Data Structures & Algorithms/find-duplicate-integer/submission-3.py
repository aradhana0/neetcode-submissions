class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        slow2 = nums[0]
        
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

        # Sol2
        # arr = [0 for _ in range(10001)]

        # for num in nums:
        #     if arr[num] > 0:
        #         return num
        #     arr[num] += 1

        # Sol 1
        # hashSet = set()
        # for num in nums:
        #     if num in hashSet:
        #         return num
        #     hashSet.add(num)

         