# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = queue.Queue()
        q.put((root, 0))
        ans = defaultdict(list)
        while not q.empty():
            node, col = q.get()
            ans[col].append(node.val)
            if node.left:
                q.put((node.left, col - 1))
            if node.right:
                q.put((node.right, col + 1))
        return [y for x, y in sorted(ans.items())]