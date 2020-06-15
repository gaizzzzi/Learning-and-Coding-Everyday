"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph_beat_94(self, node: 'Node') -> 'Node':
        # 16:28 - 16:40
        if not node:
            return None
        node_map = {}
        def dfs_helper(node):
            if not node.val in node_map:
                new_node = Node(node.val, [])
                node_map[node.val] = new_node
            
                for neighbor in node.neighbors:
                    node_map[node.val].neighbors.append(dfs_helper(neighbor))
            
            return node_map[node.val]
        return dfs_helper(node)
                