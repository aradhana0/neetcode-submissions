import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sort_list(pairs, s, e):
            if s >= e:
                return

            left = right = s

            for i in range(s, e+1):
                if pairs[right][0] < pairs[e][0]:
                    pairs[right], pairs[left] = pairs[left], pairs[right]
                    left += 1
                right += 1
 
            pairs[left], pairs[e] = pairs[e], pairs[left]

            sort_list(pairs, s, left - 1)
            sort_list(pairs, left + 1, e)


        if len(points) == 0 or k == 0:
            return []

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            distance = math.sqrt((x1)**2 + (y1)**2)
            
            points[i] = (distance, points[i])

        sort_list(points, 0, len(points) - 1)

        answer = []

        for i in range(k):
            answer.append(points[i][1])

        return answer