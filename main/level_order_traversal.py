
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def level_order_traversal:
        if not root:
            return []
        queue = [root]
        level_order_val = []
        while queue:
            temp = []
            for q in queue:
		level_order_val.append(q.val)
                if q.left:
                    temp.append(q.left)
                if q.right:
                    temp.append(q.right)
	    queue = temp
        return level_order_vals
	
    
	
        