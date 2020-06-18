import queue
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        var_map = {}
        for i, var in enumerate(equations):
            var1, var2 = var
            var_map[var1] = var_map.get(var1, []) + [(var2, values[i])]
            var_map[var2] = var_map.get(var2, []) + [(var1, 1 / values[i])]
        
        def bfs_helper(var1, var2):
            q = queue.Queue()
            q.put((var1, 1))
            visited = set()
            while not q.empty():
                n = q.qsize()
                while n:
                    n -= 1
                    var, prod = q.get()
                    if not var in var_map:
                        continue
                    for tmp_var, value in var_map[var]:
                        if tmp_var == var2:
                            return value * prod
                        if not tmp_var in visited:
                            visited.add(tmp_var)
                            q.put((tmp_var, value * prod))
            return -1.0
        
        ans = []
        for var1, var2 in queries:
            if not var1 in var_map or not var2 in var_map:
                ans.append(-1.0)
            else:
                ans.append(bfs_helper(var1, var2))
            
        return ans
                