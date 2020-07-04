# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # almost one pass with typo
        def findleftmost(root):
            if not root.left:
                return root
            left = findleftmost(root.left)
            if root.left == left:
                root.left = left.right
            return left
            
        if not root:
            return None
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        if root.val == key:
            if not root.right or not root.left:
                return root.left or root.right
            else:
                # find left most node od right child
                tmp = findleftmost(root.right)
                if tmp != root.right:
                    tmp.right = root.right
                tmp.left = root.left
            return tmp
                    
        return root