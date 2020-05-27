class Solution:
    def mergeTrees_editing_existing_Tree_88ms(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    	# this runs much faster than creating new trees
        if not t1:
            return t2
        if not t2:
            return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
                                   
        return t1
    def mergeTrees_creating_new_tree_100ms(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        return TreeNode(t1.val + t2.val, 
                        self.mergeTrees(t1.left, t2.left), 
                        self.mergeTrees(t1.right, t2.right))