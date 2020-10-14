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
    def flatten(self, head: 'Node') -> 'Node':
        def helper(node):
            while node:
                if node.child: 
                    nodenext = node.next
                    tail = helper(node.child)
                    node.next, node.child.prev = node.child, node
                    node.child = None
                    tail.next = nodenext
                    if nodenext:
                        nodenext.prev = tail
                if not node.next:
                    return node
                node = node.next
        helper(head)
        return head

class Solution:
    def flatten_iterative(self, head: 'Node') -> 'Node':
        if not head:
            return None
        pseudohead = Node(0,None,head,None)
        prev = pseudohead
        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        head.prev = None
        
        return head