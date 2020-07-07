# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def is_same(s_node, t_node):
            if not s_node and not t_node:
                return True
            elif not s_node or not t_node:
                return False
            
            if s_node.val == t_node.val:
                return is_same(s_node.left, t_node.left) and is_same(s_node.right, t_node.right)
        
        def traversal(s_node, t_node):
            if is_same(s_node, t_node):
                return True
            return s_node and (traversal(s_node.left, t_node) or traversal(s_node.right, t_node))
        
        return traversal(s, t)