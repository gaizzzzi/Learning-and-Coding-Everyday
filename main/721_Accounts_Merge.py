class union_find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, _x, _y):
        x, y = self.find(_x), self.find(_y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.rank[y] += 1
        elif self.rank[x] < self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1
        elif x < y:
            self.parent[y] = x
            self.rank[x] += 1
        else:
            self.parent[x] = y
            self.rank[y] += 1
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find
        # 17:06 - 17:40
        uf = union_find(len(accounts))
        emails_map = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if not emails_map.get(email) is None:
                    uf.union(emails_map[email], i)
                emails_map[email] = i
        
        accounts_map = {}
        sorted_email = sorted(emails_map.items())
        for email, i in sorted(sorted_email):
            parent_i = uf.find(i)
            accounts_map[parent_i] = accounts_map.get(parent_i, []) + [email]
            
        return [[accounts[i][0]] + emails for i, emails in accounts_map.items()]
            
            
            
       
                
            
        
        
        
            
                    