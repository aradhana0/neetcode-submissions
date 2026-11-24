# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort_list(pairs, s, e):
            if s >= e:
                return
            # pivot = pairs[e]
            left = right = s

            for i in range(s, e+1):
                if pairs[right].key < pairs[e].key:
                    pairs[right], pairs[left] = pairs[left], pairs[right]
                    left += 1
                right += 1
 
            pairs[left], pairs[e] = pairs[e], pairs[left]

            sort_list(pairs, s, left - 1)
            sort_list(pairs, left + 1, e)

            # return pairs

        sort_list(pairs, 0, len(pairs) - 1)
        return pairs