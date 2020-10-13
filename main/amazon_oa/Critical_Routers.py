class unionfind:
    def __init__(self, n = 0):
        self.prt = [i for i in range(n)]

    def find(self, x):
        while x != self.prt[x]:
            self.prt[x] = self.prt[self.prt[x]]
            x = self.prt[x]
        return x

    def union(self, x, y):
        self.prt[self.find(x)] = self.find[y]

    def is_all_connected(self):
        if len(set([self.find(node) for node in self.prt])) == 1:
            return True

def critial_routers(numNodes, numEdges, edges):
    graph_map = defaultdict(list)
    for u, v in edges:
        graph_map[u].append(v)
        graph_map[v].append(u)

    def uf_helper(graph_map, remove_node):
        uf = unionfind(len(graph_map) - 1)
        for node in range(numNodes):
            if node == remove_node:
                continue
            for next_node in graph_map[node]:
                if next_node == remove_node:
                    continue
                uf.union(node, next_node)
        return uf.is_all_connected()

    res = []
    for node in range(numNodes):
        if uf_helper(graph_map, node):
            res.append(node)
            
    return res
