class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if target == nums[mid]:
                return mid 

            if nums[mid] >= nums[L]:
                if target < nums[mid] and target >= nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
            elif nums[mid] < nums[R] :
                if target > nums[mid] and target <= nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                return -1

        return -1
            