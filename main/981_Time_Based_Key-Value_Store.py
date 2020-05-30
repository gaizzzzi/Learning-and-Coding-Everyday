class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_list = []
           
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_list.append((timestamp, key, value))
        
    def get(self, key: str, timestamp: int) -> str:
        start, end = 0, len(self.time_list) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.time_list[mid][0] == timestamp:
                break
            if self.time_list[mid][0] < timestamp:
                start = mid
            else:
                end = mid
        if self.time_list[start][0] > timestamp:
            return ""
        elif self.time_list[start][0] <= timestamp < self.time_list[end][0]:
            mid = start
        else:
            mid = end
        while mid > -1 and self.time_list[mid][1] != key:
            mid -= 1
        if mid == -1:
            return ""
        return self.time_list[mid][2]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)