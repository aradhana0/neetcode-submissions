class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].append([value, timestamp])
        else:
            self.time_map[key] = [[value, timestamp]]
            
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        if timestamp < self.time_map[key][0][1]:
            return ""

        n = len(self.time_map[key]) - 1

        l = 0
        r = n


        while l < r:
            mid = (l + r + 1)//2

            if self.time_map[key][mid][1] <= timestamp:
                l = mid

            elif self.time_map[key][mid][1] > timestamp:
                r = mid - 1

        return  self.time_map[key][l][0]
