class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def inorder_successor(root, p): # return successor of p
	if not root:
		return None
	# if p.right:
	#	find the leftmost child of p.right
	# elif not p.right and p_parent.left == p:
	# 	return p's parent
	# else: # not p.right and p_parent.right == p or p dont have a parent:
	#	return None

	if root.val < p.val:
		res = inorder_successor(root.right, p)
		return res if res != p else None
	elif root.val > p.val:
		res = inorder_successor(root.left)
		return res if res != p else root
	else:
		if root.right:
			return find_leftmost(root.right, p)
		else:
			return root

def find_leftmost(root):
	if root.left:
		return find_leftmost(root.left)
	else:
		return root
