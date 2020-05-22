
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def build_tree(self, l) -> TreeNode:
        if not list:
            return None

        hashmap = {}
        root = TreeNode(l[0])
        hashmap[0] = root
        
        i = 0
        j = 1
        while j < len(l):
            if l[i] != "null":
                root = hashmap[i]
            if j < len(l) and l[j] != "null":
                left = TreeNode(l[j])
                root.left = left
                hashmap[j] = left
            j += 1
            if j < len(l) and l[j] != "null":
                right = TreeNode(l[j])
                root.right = right
                hashmap[j] = right
            j += 1
            i += 1
        return hashmap[0]
            
            
    def level_order(self, root: TreeNode) -> [[]]:
        if not root:
            return []
        queue = [root]
        level_order_vals = []
        while queue:
            temp = []
            level = []
            for q in queue:
                level.append(q.val)
                if q.left:
                    temp.append(q.left)
                if q.right:
                    temp.append(q.right)
            queue = temp
            level_order_vals.append(level)
        return level_order_vals

#test
T = Tree()
tree = T.build_tree([3,9,20,"null","null",15,7])
print(T.level_order(tree))
	
        