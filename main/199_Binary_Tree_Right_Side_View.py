# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    
    def rightSideView(self, root: TreeNode) -> List[int]:
        # 17:38 - 17:43
        if not root:
            return []
        q = queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            n = q.qsize()
            tmp = []
            while n:
                node = q.get()
                tmp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                n -= 1
            ans.append(tmp[-1])
        return ans

    def rightSideView_dfs(self, root: TreeNode) -> List[int]:
        # 17:49 - 17:51
        ans = []
        def helper(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
        helper(root, 0)
        return ans