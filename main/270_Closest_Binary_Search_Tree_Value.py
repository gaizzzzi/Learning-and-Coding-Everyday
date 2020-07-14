# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def helper(node, minmax, target):
            if not node:
                return
            if node.val > target:
                minmax[1] = min(node.val, minmax[1])
                helper(node.left, minmax, target)
            else:
                minmax[0] = max(node.val, minmax[0])
                helper(node.right, minmax, target)
        minmax = [float('-inf'), float('inf')]
        helper(root, minmax, target)
        if abs(minmax[1] - target) <= abs(minmax[0] - target):
            return minmax[1]
        else:
            return minmax[0]