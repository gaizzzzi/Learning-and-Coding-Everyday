# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root):
            if not root:
                return True, None, None
                
            is_l_valid, l_min, l_max = helper(root.left)
            is_r_valid, r_min, r_max = helper(root.right)
            
            is_valid = is_l_valid and is_r_valid \
                        and (not r_min or root.val < r_min.val) \
                        and (not l_max or root.val > l_max.val)
            
            return(is_valid, 
                   l_min if l_min else root, 
                   r_max if r_max else root)
        
        return helper(root)[0]