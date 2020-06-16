# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # 17:09 - 17:24
        ans = []
        def dfs_helper(root):
            if not root:
                return None
            
            root.left = dfs_helper(root.left)
            root.right = dfs_helper(root.right)
            
            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None
            
            return root
            
        if not root.val in to_delete:
            ans.append(root)
        
        dfs_helper(root)
        return ans
            
            