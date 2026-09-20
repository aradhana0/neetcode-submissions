class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        sortedList = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        for i in range(k):
            res.append(sortedList[i][0])

        return res