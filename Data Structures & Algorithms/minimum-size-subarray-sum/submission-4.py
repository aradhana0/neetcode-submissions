class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        answer = float('inf')
        i = 0
        for j in range(len(nums)):
            if sum < target:
                sum += nums[j]

            while sum >= target:
                print(i, j, sum, answer)
                answer = min(answer, j - i + 1)
                sum -= nums[i]
                i += 1

        return answer if answer != float('inf') else 0