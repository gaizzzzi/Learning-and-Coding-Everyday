class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
    node_list = []
    def helper(root, x, y):
        if not root:
            return
        node_list.append((x, y, root.val))
        helper(root.left, x - 1, y + 1)
        helper(root.right, x + 1, y + 1)
    helper(root, 0, 0)
    res = []
    prev = float("-inf")
    for x, y, val in sorted(node_list):
        if prev != x:
            res.append([])
        res[-1].append(val)
        prev = x
    return res