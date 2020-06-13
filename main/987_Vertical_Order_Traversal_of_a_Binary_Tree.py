# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 16:03 - 16:25
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        tree_map = {}
        def helper(root, x, y):
            if not root:
                return
            tree_map[(x, y)] = tree_map.get((x, y), []) + [root.val]
            tree_map[(x, y)].sort()
            
            helper(root.left, x - 1, y + 1)
            helper(root.right, x + 1, y + 1)
            
        helper(root, 0, 0)
        sort_keys = sorted(tree_map.keys())
        ans = []
        pre_x = None
        tmp = []
        for x, y in sort_keys:
            if pre_x is None or pre_x == x:
                tmp.extend(tree_map[(x, y)])
            else:
                ans.append(tmp)
                tmp = tree_map[(x, y)]
            pre_x = x
        ans.append(tmp)
        return ans
        