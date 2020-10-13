class treeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nums):
    if not nums:
        return None
    mid_idx = len(nums) // 2
    return treeNode(nums[mid_idx], build_tree(nums[:mid_idx]), build_tree(nums[mid_idx + 1:]))

def find_lca(root, node1, node2):
    if not root:
        return None, False, False

    left, left_node1_found, left_node2_found = find_lca(root.left, node1, node2)
    right, right_node1_found, right_node2_found = find_lca(root.right, node1, node2)

    node1_found = left_node1_found or right_node1_found or root.val == node1
    node2_found = left_node2_found or right_node2_found or root.val == node2

    if (left and right) or (root.val == node1 or root.val == node2):
        return root, node1_found, node2_found
    elif left or right:
        return left or right, node1_found, node2_found
    else:
        return None, False, False

def get_distance(ancestor, offspring):
    if ancestor.val == offspring:
        return 0
    if ancestor.val > offspring:
        return 1 + get_distance(ancestor.left, offspring)
    else:
        return 1 + get_distance(ancestor.right, offspring)


def solver(nums, node1, node2):
    # build tree
    root = build_tree(nums)

    # find lowest common ancestor
    ancestor, node1_found, node2_found = find_lca(root, node1, node2)
    if not (node1_found and node2_found):
        return -1

    # get distance
    return get_distance(ancestor, node1) + get_distance(ancestor, node2)

print(solver([1,2,3], 1, 8))