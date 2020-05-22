
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def build_tree(self, input_list) -> TreeNode:
        if not input_list:
            return None

        treenode_map = {}
        root = TreeNode(input_list[0])
        treenode_map[0] = root
        
        i = 0
        j = 1
        while j < len(input_list):
            if input_list[i] != "null":
                root = treenode_map[i]
            if j < len(input_list) and input_list[j] != "null":
                left = TreeNode(input_list[j])
                root.left = left
                treenode_map[j] = left
            j += 1
            if j < len(input_list) and input_list[j] != "null":
                right = TreeNode(input_list[j])
                root.right = right
                treenode_map[j] = right
            j += 1
            i += 1
        return treenode_map[0]
            
            
    def level_order(self, root: TreeNode) -> [[]]:
        if not root:
            return []
        queue = [root]
        level_order_vals = []
        n = len(queue)
        level = []
        while n:
            q = queue.pop(0)
            level.append(q.val)
            if q.left:
                queue.append(q.left)
            if q.right:
                queue.append(q.right)
            n -= 1
            if n == 0:
                level_order_vals.append(level)
                level = []
                n = len(queue)
        return level_order_vals

#test
T = Tree()
tree = T.build_tree([3,9,20,"null","null",15,7])
print(T.level_order(tree))
	
        