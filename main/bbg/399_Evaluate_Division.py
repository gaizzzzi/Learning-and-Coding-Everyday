class Solution:
    def calcEquation_dfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        node_map = defaultdict(defaultdict)
        for (num1, num2), val in zip(equations, values):
            node_map[num1][num2] = val
            node_map[num2][num1] = 1/val
        
        # dfs
        def helper(curr, dst, visited):
            if dst in node_map[curr]:
                return node_map[curr][dst]
            for next_node in node_map[curr].keys():
                if not next_node in visited:
                    visited.add(next_node)
                    val = helper(next_node, dst, visited)
                    visited.remove(next_node)
                    if val:
                        node_map[curr][dst] = val * node_map[curr][next_node]
                        node_map[dst][curr] = 1 / node_map[curr][dst]
                        return node_map[curr][dst]
            return 0
        
        res = []
        for var1, var2 in queries:
            ans = helper(var1, var2, set())
            if ans:
                res.append(ans)
            else:
                res.append(-1)
        return res

import queue
class Solution:
    def calcEquation_bfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        node_map = defaultdict(defaultdict)
        for (num1, num2), val in zip(equations, values):
            node_map[num1][num2] = val
            node_map[num2][num1] = 1/val
        
        # bfs
        def helper(src, dst):
            q = queue.Queue()
            q.put((src, 1))
            visited = {src}
            while not q.empty():
                curr, val = q.get()
                for next_node in node_map[curr]:
                    if next_node == dst:
                        return val * node_map[curr][next_node]
                    if not next_node in visited:
                        visited.add(next_node)
                        q.put((next_node, val * node_map[curr][next_node]))
            return -1

        return [helper(var1, var2) for var1, var2 in queries]