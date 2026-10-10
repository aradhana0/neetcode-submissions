class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if len of nums == 1 -> return False
        # two pointers for window boundary - start = 0, end = start + 1
        # iterate and store in set if not already present
        # if present, check the condition abs(start - end) <= 0
        # check boundary. if reached, shift the window, remove the start - 1 from the set

        if len(nums) == 1: return False

        start = 0
        end = start
        visited = set()

        while end < len(nums):
            if abs(start - end) <= k: 
                if nums[end] not in visited:
                    visited.add(nums[end])
                    end += 1
                else:
                    return True
            else:
                visited.remove(nums[start])
                start += 1

        return False
