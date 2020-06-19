# 00:30 - 01:07
class unionfind:
    # 00:30 - 00:34
    def __init__(self, m, n):
        self.prt = [i for i in range(m * n + 1)]
        self.sz = [1 for _ in range(m * n + 1)]
        
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x

    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return
        if y < x:
            self.prt[y] = x
            self.sz[x] += self.sz[y]
        else:
            self.prt[x] = y
            self.sz[y] += self.sz[x]
    
    def top(self):
        return self.sz[-1]
        
        
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fall = [-1] * len(hits)
        m, n = len(grid), len(grid[0])
        uf = unionfind(m, n)
        
        for i, (x, y) in enumerate(hits):
            if not grid[x][y]:
                fall[i] = 0
            grid[x][y] = 0
            
        for i, row in enumerate(grid):
            for j, brick in enumerate(row):
                if brick:
                    if i and grid[i - 1][j]:
                        uf.union((i - 1) * n + j, i * n + j)
                    if j and grid[i][j - 1]:
                        uf.union(i * n + j, i * n + j - 1)
                    if not i:
                        uf.union(i * n + j, m * n)
        
        pre_top = uf.top()
        for i, (_x, _y) in enumerate(hits[::-1]):
            if not fall[len(hits) - i - 1]:
                continue
            if not _x and not _y:
                a = 1
            if not _x:
                uf.union(_x * n + _y, m * n)
            for dx, dy in neighbors:
                x, y = _x + dx, _y + dy
                if -1 < x < m and -1 < y < n and grid[x][y]:
                    uf.union(_x * n + _y, x * n + y)
                    
            grid[_x][_y] = 1
            cur_top = uf.top()
            fall[len(hits) - i - 1] =  max((cur_top - pre_top - 1), 0)
            pre_top = cur_top
            
        return fall
            
                    
        