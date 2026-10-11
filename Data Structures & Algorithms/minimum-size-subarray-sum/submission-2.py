class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        answer = float('inf')
        start = 0

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                answer = min(answer, end - start + 1)
                total -= nums[start]
                start += 1

        return answer if answer != float('inf') else 0