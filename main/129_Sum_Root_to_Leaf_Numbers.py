# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # 23:25 - 23:28
        if not root:
            return 0
        self.sum = 0
        def helper(root, num):
            if not root.left and not root.right:
                self.sum += num * 10 + root.val
            if root.left:
                helper(root.left, num * 10 + root.val)
            if root.right:
                helper(root.right, num * 10 + root.val)
        helper(root, 0)
        return self.sum