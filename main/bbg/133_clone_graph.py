class Node:
    def __init__(self, val, neighbors = []):
        self.val = val
        self.neighbors = neighbors

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None
    new_node = Node(node.val, [])
    node_map = {node.val: new_node}
    def helper(node):
        for neighbor in node.neighbors:
            if not neighbor.val in node_map:
                new_neighbor = Node(neighbor.val, [])
                node_map[neighbor.val] = new_neighbor
                helper(neighbor)
            node_map[node.val].neighbors.append(node_map[neighbor.val])
    helper(node)
    
    return new_node