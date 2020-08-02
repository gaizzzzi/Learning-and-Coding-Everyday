"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten_change_inplace(self, head: 'Node') -> 'Node':
        def helper(node):
            if node.child:
                childtail = helper(node.child)
                childtail.next = node.next
                if node.next:
                    node.next.prev = childtail
                node.next, node.child.prev = node.child, node
                node.child = None
            if node.next:
                return helper(node.next)
            return node
        if head:
            helper(head)
        return head