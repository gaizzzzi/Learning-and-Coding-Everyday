import queue
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = {(0, 0)}
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        q = queue.Queue()
        q.put((0, 0, 0)) # (x, y, step)
        
        while not q.empty():
            _i, _j, _step = q.get()
            if _i == x and _j == y:
                return _step
            for di, dj in directions:
                i, j = _i + di, _j + dj
                if not (i, j) in visited and not ((x - i) > 0 and (y - j) > 0):
                    visited.add((i, j))
                    q.put((i, j, _step + 1))
        
import queue
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        x, y = abs(x), abs(y)
        visited1, visited2 = {(0, 0):0}, {(x, y):0}
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        q1, q2 = queue.Queue(), queue.Queue()
        q1.put((0, 0, 0)) # (x, y, step)
        q2.put((x, y, 0))
        while not q1.empty() and not q2.empty():
            i1, j1, step1 = q1.get()
            i2, j2, step2 = q2.get()
            
            for di, dj in directions:
                ni1, nj1 = i1 + di, j1 + dj
                ni2, nj2 = i2 + di, j2 + dj
                
                if (ni1, nj1) in visited2:
                    return step1 + 1 + visited2[(ni1, nj1)]
                if  (ni2, nj2) in visited1:
                    return visited1[(ni2, nj2)] + step2 + 1
                
                if not (ni1, nj1) in visited1 and (x - ni1 > 0 and y - nj1 > 0):
                    visited1[(ni1, nj1)] = step1 + 1
                    q1.put((ni1, nj1, step1 + 1))
                if not (ni2, nj2) in visited2:
                    visited2[(ni2, nj2)] = step2 + 1
                    q2.put((ni2, nj2, step2 + 1))
                
            
            
            