class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        result = []
        res = [[] for _ in range(length)]
        freq = Counter(nums)

        for key,v in freq.items():
            res[v - 1].append(key)

        for i in range(length - 1, -1, -1):
            if res[i] != [] and k > 0:
                for j in res[i]: 
                    result.append(j)
                    k -= 1
            if k == 0:
                return result