class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutation = []
        result = []
        visited = [False for i in range(21)]
        def bt():
            if len(nums) == len(permutation):
                result.append(permutation.copy())

            for num in nums:
                if visited[num + 10] == True:
                    continue

                visited[num + 10] = True
                permutation.append(num)

                bt()

                visited[num + 10] = False
                permutation.pop()

        bt()

        return result