class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combination = []
        candidates.sort()

        def bt(i, total):
            # success
            if total == target:
                result.append(combination.copy())
                return
            # invalid path
            if i >= len(candidates) or total > target:
                return


            combination.append(candidates[i])
            bt(i + 1, total + candidates[i])

            combination.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            bt(i + 1, total)

        bt(0, 0)

        return result