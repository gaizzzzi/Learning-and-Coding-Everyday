# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        queue = [root]
        tree_list = []
        while queue:
            n = len(queue)
            while n:
                node = queue.pop(0)
                if node == "null":
                    tree_list.append(node)
                else:    
                    if node.val != None:
                        tree_list.append(str(node.val))
                        if node.left:
                            queue.append(node.left)
                        else:
                            queue.append("null")
                        if node.right:
                            queue.append(node.right)
                        else:
                            queue.append("null")
                n -= 1
        #print("[" + ",".join(tree_list) + "]")
        return "[" + ",".join(tree_list) + "]"


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None

        tree_list = data[1:-1].split(",")
        #print(tree_list)
        treenode_map = {}
        treenode_map[0] = TreeNode(tree_list[0])

        i, j = 0, 1
        
        while j < len(tree_list) and i < len(tree_list):
            while i < len(tree_list) and tree_list[i] == "null":
                i += 1
            #print(i)
            if i < len(tree_list) and tree_list[i] != "null":
                node = treenode_map[i]

            if j < len(tree_list) and tree_list[j] != "null":
                node.left = TreeNode(tree_list[j])
                treenode_map[j] = node.left

            j += 1

            if j < len(tree_list) and tree_list[j] != "null":
                node.right = TreeNode(tree_list[j])
                treenode_map[j] = node.right
            
            j += 1
            i += 1
        return treenode_map[0]

            


                



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))