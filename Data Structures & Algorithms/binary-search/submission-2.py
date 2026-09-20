class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        def findItemIndex(L, R):
            if L > R: 
                return -1
            mid = (L + R) // 2

            if target > nums[mid]:
                return findItemIndex(mid + 1, R)
            elif target < nums[mid]:
                return findItemIndex(L, mid - 1)
            else:
                return mid
        
        
        return findItemIndex(L, R)