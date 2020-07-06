class Tree:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def question1(self, root):
		self.maxlen = 0
		def helper(root):
			# returns max depth of root
			if not root:
				return 0
			left_depth = helper(root.left)
			right_depth = helper(root.right)
			self.maxlen = max(self.maxlen, left_depth + right_depth)
			return max(left_depth, right_depth) + 1

		depth = helper(root)
		return self.maxlen