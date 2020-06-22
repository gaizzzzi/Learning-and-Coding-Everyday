# kruskal 18:50 - 18:57
class unionfind:
    def __init__(self, n):
        self.prt = [i for i in range(n)]
        self.rk = [0 for _ in range(n)]
        self.valid_edge = 0
        
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return 
            
        self.valid_edge += 1
        if self.rk[x] < self.rk[y]:
            self.prt[x] = y
            self.rk[y] += 1
        else:
            self.prt[y] = x
            self.rk[x] += 1
    
    def uconnected(self):
        return len(self.prt) - self.valid_edge - 1
        
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = unionfind(n)
        for x, y in connections:
            uf.union(x, y)
        
        return uf.uconnected()

# prim 19:09 - 19:16
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        adjacent = {}
        for x, y in connections:
            adjacent[x] = adjacent.get(x, []) + [y]
            adjacent[y] = adjacent.get(y, []) + [x]
        
        def connect_helper(x):
            if not x in adjacent:
                return
            for y in adjacent[x]:
                if not y in visited:
                    visited.add(y)
                    connect_helper(y)
        
        visited = set()
        set_count = -1
        for i in range(n):
            if not i in visited:
                set_count += 1
                visited.add(i)
                connect_helper(i)
        return set_count
                
        
        
        
        
        
        
        