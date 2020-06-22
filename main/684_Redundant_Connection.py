# 18:23 - 18:30
class unionfind:
    def __init__(self, n):
        self.prt = [i for i in range(n + 1)]
        self.rk = [0 for _ in range(n + 1)]
    
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]] 
            x = self.prt[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return False
        
        if self.rk[x] > self.rk[y]:
            self.prt[y] = x
            self.rk[x] += 1
        else:
            self.prt[x] = y
            self.rk[y] += 1
            
        return True
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = unionfind(len(edges))
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]