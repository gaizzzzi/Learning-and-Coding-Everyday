# The read4 API is already defined for you.
# def read4(buf: List[str]) -> int:
import queue
class Solution:
    def __init__(self):
        self.q = queue.Queue()
    def read(self, buf: List[str], n: int) -> int:
        pos = 0
        while pos < n:
            if self.q.empty():
                tmp = [' '] * 4
                _n = read4(tmp)
                [self.q.put(x) for x in tmp[:_n]]
            if self.q.empty():
                return pos
            while not self.q.empty() and pos < n:
                buf[pos] = self.q.get()
                pos += 1
        return pos
            
        
        