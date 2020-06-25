# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.idx = 0
        self.ans = []
        def helper(root):
            if not root:
                return
            if root.val != voyage[self.idx]:
                self.ans = [-1]
                return
            self.idx += 1
            if self.idx < len(voyage) and root.left and root.left.val != voyage[self.idx]:
                self.ans.append(root.val)
                helper(root.right)
                helper(root.left)
                
            else:
                helper(root.left)
                helper(root.right)
                
        helper(root)
        return self.ans
                
                