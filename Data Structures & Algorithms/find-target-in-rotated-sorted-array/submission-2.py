class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        def findMinIdx(L, R):
            while L < R:
                mid = (L + R) // 2

                if nums[mid] < nums[R]:
                    R = mid
                else:
                    L = mid + 1
            return L

        minIdx = findMinIdx(L, R)
        # print(L, R)

        if target >= nums[minIdx] and target <= nums[-1]:
            L = minIdx
            R = len(nums) - 1
        else:
            L = 0
            R = minIdx - 1
        # print(L, R)
        while L < R: 
            mid = (L + R) // 2

            if target < nums[mid]:
                R = mid - 1
            elif target > nums[mid]:
                L = mid + 1
            else:
                return mid
            # elif target == nums[mid]:
            #     return mid
            # else: return -1

        if target == nums[L]:
            return L
        return -1