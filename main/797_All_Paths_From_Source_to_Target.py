class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # build the graph using hashmap
        graph_map = {}
        for i, neibors in enumerate(graph):
            graph_map[i] = neibors
        target = len(graph) - 1
        memo = collections.defaultdict(list) # key = node, value = [[]] list of paths from node to target
        
        # dfs search
        def dfs_helper(node, target):
            if node == target:
                return [[node]]
            for next_node in graph_map.get(node):
                if not next_node in memo:
                    memo[next_node] = dfs_helper(next_node, target)
                memo[node].extend([[node] + path for path in memo[next_node]])
            return memo[node]
        return dfs_helper(0, target)