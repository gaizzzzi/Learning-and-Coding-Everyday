# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor_ordinary(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 20:53 - 20:56
        def helper(root):
            if not root:
                return None
            if root == p:
                return p
            if root == q:
                return q
            left = helper(root.left)
            right = helper(root.right)
            if left and right:
                return root
            elif left:
                return left
            elif right:
                return right
            else:
                return None
            
        return helper(root)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 21:58 - 21:08
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root