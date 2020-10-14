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
            return []
        node_map = defaultdict(list) # {column_idx: [list of vals]}
        q = queue.Queue() #[(node, column)]
        q.put((root, 0))
        mincol, maxcol = float('inf'), float('-inf')
        while not q.empty():
            node, col = q.get()
            mincol, maxcol = min(mincol, col), max(maxcol, col)
            node_map[col].append(node.val)
            if node.left:
                q.put((node.left, col - 1))
            if node.right:
                q.put((node.right, col + 1))
        return [node_map[col] for col in range(mincol, maxcol + 1)]
        