class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        val = preorder[0]
        segment = inorder.index(val)
        left = self.buildTree(preorder[1: segment + 1], inorder[:segment])
        right = self.buildTree(preorder[segment + 1:], inorder[segment + 1:])
        return TreeNode(val, left, right)