# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 15:54 - 15:57
        self.diameter = 0
        def helper(root):
            if not root:
                return -1
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            self.diameter = max(self.diameter, left + right)
            return max(left, right)
        helper(root)
        return self.diameter