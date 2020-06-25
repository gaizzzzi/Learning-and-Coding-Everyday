# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 20:25-20:28
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def helper(root):
            if not root:
                return
            helper(root.right)
            self.sum += root.val
            root.val = self.sum
            helper(root.left)
        helper(root)
        return root
            