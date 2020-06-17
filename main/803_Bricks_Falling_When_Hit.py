# ans1 
# 21:21 - 00:33
class unionfind:
    def __init__(self, m, n, d):
        self.parent = [i for i in range(n * m)]
        self.amount = []
        for row in d:
            for x in row:
                self.amount.append(x)
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
             return
        if x < y:
            self.parent[y] = x
            self.amount[x] += self.amount[y]
            self.amount[y] = 0 
        else:
            self.parent[x] = y
            self.amount[y] += self.amount[x]
            self.amount[x] = 0
        
class Solution:
    
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        fall = [-1] * len(hits)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(hits)):
            if grid[hits[i][0]][hits[i][1]] == 0:
                fall[i] = 0
            grid[hits[i][0]][hits[i][1]] = 0
        
        def uf_helper(_x, _y):
            for dx, dy in directions:
                x, y = _x + dx, _y + dy
                if -1 < x < len(grid) and -1 < y < len(grid[0]) and \
                   grid[x][y]:
                    uf.union(_x * len(grid[0]) + _y, x * len(grid[0]) + y)
        
        # build initial union cricles
        uf = unionfind(len(grid), len(grid[0]), grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] :
                    uf_helper(i, j)
                    
        # add back brick reversely and check how many get unioned
        pre_top_amount = sum(uf.amount[:len(grid[0])])
        for i in range(len(hits) - 1, -1, -1):
            if fall[i] == 0:
                continue
            
            visited = set()
            uf.amount[hits[i][0] * len(grid[0]) + hits[i][1]] = 1
            uf_helper(hits[i][0], hits[i][1])
            grid[hits[i][0]][hits[i][1]] = 1
            top_amount = sum(uf.amount[:len(grid[0])])
            fall[i] = max(0, top_amount - pre_top_amount - 1)
            pre_top_amount = top_amount
        return fall


