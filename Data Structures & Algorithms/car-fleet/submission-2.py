class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxPos = 0
        stk = []
        res = 0
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, reverse=True)

        for i in range(len(cars)):
            timeToReach = (target - cars[i][0])/cars[i][1]
            stk.append(timeToReach)
            if len(stk) > 1 and timeToReach <= stk[len(stk) - 2]:
                stk.pop()
            
            # print(timeToReach, stk[len(stk) - 1],cars,stk)

        return len(stk)


           