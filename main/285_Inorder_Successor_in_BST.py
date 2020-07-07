# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findleftmostnode(self, root):
        if not root:
            return None
        if not root.left:
            return root
        return self.findleftmostnode(root.left)
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root:
                return None
            left = helper(root.left) if root.val > p.val else None
            right = helper(root.right) if root.val < p.val else None
            if root == p:
                node = self.findleftmostnode(root.right)
                return node or root
            if left == p:
                return root
            if right == p:
                return right
            return left or right
        
        node = helper(root)
        if node == p:
            return None
        return node
        
        