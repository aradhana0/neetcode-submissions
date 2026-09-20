class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxC = [0] * k
        res = []
        numHash = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)

        for key in numHash:
            if len(res) < k:
                res.append(key[0])
            else:
                return res
        return res