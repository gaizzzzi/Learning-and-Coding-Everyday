# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = [(root, 0)]
        maxwidth = 1
        while q:
            maxwidth, i, tmp = max(maxwidth, q[-1][1] - q[0][1] + 1), -1, tmp
            while i < len(q) - 1:
                i += 1
                node, idx = q[i]
                if not node:
                    continue
                if (tmp and not node.left) or node.left:
                    tmp.append((node.left, 2 * idx + 1))
                if (tmp and not node.right) or node.right:
                    tmp.append((node.right, 2 * idx + 2))
                
            while tmp and tmp[-1][0] == None:
                tmp.pop()
            q = tmp
        return maxwidth