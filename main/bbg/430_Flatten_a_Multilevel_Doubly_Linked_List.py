class Node:
    def __init__(self, _val = 0, _prev = None, _next = None, _child = None):
        self.val = _val
        self.prev = _prev
        self.next = _next
        self.child = _child
def flatten(self, head: 'Node') -> 'Node':
    def helper(node):
        while node:
            if node.child:
                nodenext, node.next, node.child.prev = node.next, node.child, node
                nodechild, node.child = node.child, None
                node = helper(nodechild)
                node.next = nodenext
            if node.next:
                node.next.prev = node
                node = node.next
            else:
                break
        return node
    helper(head)
    return head