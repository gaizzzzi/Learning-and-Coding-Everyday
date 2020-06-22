class unionfind:
    def __init__(self, n):
        self.prt = [i for i in range(n)]
        self.rk = [0 for _ in range(n)]
        self.cost = 0
        self.connect = 1
        
    def find(self, x):
        while self.prt[x] != x:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x
    
    def union(self, _x, _y, w):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return
        self.cost += w
        self.connect += 1
        if self.rk[x] < self.rk[y]:
            self.prt[x] = y
            self.rk[y] += 1
        else:
            self.prt[y] = x
            self.rk[x] += 1
    
    def get_cost(self):
        if self.connect == len(self.prt):
            return self.cost
        else:
            return 0
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(x, y, w, i) for i, (x, y, w) in enumerate(edges)]
        edges.sort(key = itemgetter(2))
        
        def build_mst(include, exclude):
            uf = unionfind(n)
            if include:
                uf.union(include[0], include[1], include[2]) 
            for i, (x, y, w, _) in enumerate(edges):
                if (x, y) == exclude:
                    continue
                uf.union(x, y, w)
            return uf.get_cost()
        
        # find out the minimum cost   
        mst = build_mst(None, None)
        ans = [[],[]]
        
        for x, y, w, i in edges:
            # include ith edges to see if mst still exists
            if build_mst((x, y, w), []) == mst:
                # exclude ith edges to see if it's critical
                if build_mst([], (x,y)) == mst:
                    ans[1].append(i)
                else:
                    ans[0].append(i)
        
        return ans