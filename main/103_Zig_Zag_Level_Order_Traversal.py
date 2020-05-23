class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        zigzaglevel_vals = []
        queue = [root]
        reverse_flag = -1
        while queue:
            level = []
            reverse_flag *= -1
            n = len(queue)
            while n:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            zigzaglevel_vals.append(level[::reverse_flag])
        return zigzaglevel_vals
