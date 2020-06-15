import queue
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.n = size
        self.q = queue.Queue()
        self.avg = 0
        
    def next(self, val: int) -> float:
        tmp = None
        if self.q.qsize() == self.n:
            tmp = self.q.get()
        self.q.put(val)
        if tmp is None:
            self.avg = (self.avg * (self.q.qsize() - 1) + val) / self.q.qsize()
        else:
            self.avg = (self.avg * self.n - tmp + val) / self.n
        return self.avg