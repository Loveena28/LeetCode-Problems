class TimeMap:

    def __init__(self):
        self.timeMap = {} # key: list of [val,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key]  = []
        self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap.get(key,[])
        
        l,r = 0,len(values) - 1
        while l<=r:
            mid = l + (r-l) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)