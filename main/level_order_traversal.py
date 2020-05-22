
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def build_tree_recursive(self, input_list) -> TreeNode:
        if not input_list:
            return None
        def build_tree_helper(parent_pos, child_pos):
            #print(parent_pos, child_pos)
            if parent_pos > len(input_list) - 1:
                return None 
            if input_list[parent_pos] == "null":
                return None
            node = TreeNode(input_list[parent_pos])
            node.left = build_tree_helper(child_pos, child_pos + 2)
            node.right = build_tree_helper(child_pos + 1, child_pos + 4)
            return node
        return build_tree_helper(0, 1)


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
        
        while queue:
            n = len(queue)
            level = []
            while n:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n -= 1
            level_order_vals.append(level)
        
        return level_order_vals

#test
T = Tree()
tree = T.build_tree_recursive([3,9,20,"null","null",15,7])
print(T.level_order(tree))
tree = T.build_tree_recursive([1])
print(T.level_order(tree))
	
        