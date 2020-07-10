# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return float('inf'), float('-inf'), 0
            leftmin, leftmax, leftdiff = helper(root.left)
            rightmin, rightmax, rightdiff = helper(root.right)
            cur_min, cur_max = min(leftmin, rightmin), max(leftmax, rightmax)
            cur_diff = max(leftdiff, rightdiff, root.val - cur_min, cur_max - root.val)
            return min(cur_min, root.val), max(cur_max, root.val), cur_diff
        
        return helper(root)[2]
            
            
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root, ancestor_min, ancestor_max):
            if not root:
                return 0
            left = helper(root.left, min(ancestor_min, root.val), max(ancestor_max, root.val))
            right = helper(root.right, min(ancestor_min, root.val), max(ancestor_max, root.val))
            return max(left, right, root.val - ancestor_min, ancestor_max - root.val)
        
        return helper(root, float('inf'), float('-inf'))