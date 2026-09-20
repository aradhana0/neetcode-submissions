class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]

        while l < r:
            tempWater = min(lMax, rMax) - (height[l] if height[l] <= height[r] else height[r])
            if tempWater < 0:
                tempWater = 0
            water = water + tempWater

            if height[l] <= height[r]: 
                l += 1
                lMax = max(height[l], lMax)

            else:
                r -= 1
                rMax = max(height[r], rMax)

        return water
