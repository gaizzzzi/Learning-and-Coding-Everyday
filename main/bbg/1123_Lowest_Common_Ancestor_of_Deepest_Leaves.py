# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        deepest_leaves_set = []
        deepest_depth = 0
        def deepest_leaves(root, depth):
            if not root:
                return
            nonlocal deepest_depth, deepest_leaves_set
            if depth == deepest_depth:
                deepest_leaves_set.append(root)
            elif depth > deepest_depth:
                deepest_leaves_set = [root]
                deepest_depth = depth
            deepest_leaves(root.left, depth + 1)
            deepest_leaves(root.right, depth + 1)
        
        def lca(root, node_set): # return lca
            if not root:
                return None
            if root in node_set:
                return root
            left = lca(root.left, node_set)
            right = lca(root.right, node_set)
            if left and right:
                return root
            elif left or right:
                return left or right
            else:
                return None
        deepest_leaves(root, 0)
        return lca(root, deepest_leaves_set)
            