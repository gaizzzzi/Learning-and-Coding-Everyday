# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        
        def build_graph(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                build_graph(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                build_graph(node.right)
        ans, visited = [], {target}
        
        def traversal(node, depth):
            if depth == K:
                ans.append(node.val) 
            for neibor in graph[node]:
                
                if not neibor in visited:
                    visited.add(neibor)
                    traversal(neibor, depth + 1)
        
        build_graph(root)
        traversal(target, 0)
        return ans
        
                
                