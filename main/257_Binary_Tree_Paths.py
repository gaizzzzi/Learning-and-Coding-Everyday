# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:  
        ans = []
        def helper(root, path):
            if not root:
                return

            if not root.left and not root.right:
                ans.append("->".join(path + [str(root.val)]))

            helper(root.left, path + [str(root.val)])
            helper(root.right, path + [str(root.val)])
            
        helper(root, [])
        return ans    




