class MedianFinder:
    #18:55 - 19:15 2 heaps
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = [] # store large half of number
        self.maxheap = [] # store small half of number

    def addNum(self, num: int) -> None:
        max_val = a = min_val = c = 0
        if self.maxheap:
            max_val = -heappop(self.maxheap)
            a = min(max_val, num)
            heappush(self.maxheap, -a)
        if self.minheap:
            min_val = heappop(self.minheap)
            c = max(num, min_val)
            heappush(self.minheap, c)
            
        b = num + max_val + min_val - a - c
        
        if len(self.maxheap) > len(self.minheap):
            heappush(self.minheap, b)
        else:
            heappush(self.maxheap, -b)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()