class unionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.parent[self.find(x)] = self.find(y)
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map = {}
        uf = unionFind(len(accounts))
        for i in range(len(accounts)):
            name, e_address = accounts[i][0], accounts[i][1:]
            for email in e_address:
                if email in email_map:
                    uf.union(email_map[email], i)
                email_map[email] = uf.find(i)
        accounts_map = defaultdict(set)
        for i in range(len(accounts)):
            tmp = accounts[i][1:]
            accounts_map[uf.find(i)].update(set(tmp))
        return [[accounts[i][0]] + sorted(accounts_map[i]) for i in accounts_map.keys()]
        
        