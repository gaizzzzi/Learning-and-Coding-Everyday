class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def helper(node, pre_node, rank):
            rk[node], ans = rank, []
        
            for next_node in neighbors[node]:
                if next_node == pre_node:
                    continue
                    
                if not rk[next_node]:
                    ans += helper(next_node, node, rank + 1)
                
                rk[node] = min(rk[node], rk[next_node])
                if rk[next_node] > rank:
                    ans.append([node, next_node])
            return ans
        
        neighbors, rk = [[] for _ in range(n)], [0] * n 
        for x, y in connections:
            neighbors[x].append(y)
            neighbors[y].append(x)
            
        return helper(0, -1, 1) #node, pre_node, rank