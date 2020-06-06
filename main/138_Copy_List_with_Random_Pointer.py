"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 19:03 - 19:17
        # add new node next to original node A -> A' -> B -> B' -> ...
        if not head:
            return None
        node = head
        
        while node:
            new_node = Node(node.val, node.next)
            node.next = new_node
            node = new_node.next
        
        # add the random links
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next
        
        # split the new nodes out
        node = head.next
        while node.next:
            node.next = node.next.next
            node = node.next
        return head.next
        