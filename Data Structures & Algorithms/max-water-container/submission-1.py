class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        maxArea = 0
        while s < e:
            area = min(heights[s], heights[e]) * (e - s)
            maxArea = max(area, maxArea)
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1

        return maxArea
