class unionfind:
    def __init__(self, n):
        self.prt = [i for i in range(n)]
        self.rk = [1 for i in range(n)]
    
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return
        if self.rk[x] < self.rk[y]:
            self.prt[x] = y
            self.rk[y] += 1
        else:
            self.prt[y] = x
            self.rk[x] += 1
    
    def is_path(self):
        return self.find(0) == self.find(len(self.prt) - 1)
        
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        hp = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                heappush(hp, (-A[i][j], (i, j)))
        
        uf = unionfind(len(A) * len(A[0]))
        
        maxmin = 0
        while not uf.is_path() and hp:
            val, (i, j) = heappop(hp)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if -1 < ni < len(A) and -1 < nj < len(A[0]) and A[ni][nj] >= -val: 
                    uf.union(i * len(A[0]) + j, ni * len(A[0]) + nj)
            maxmin = -val
        return maxmin
        
        