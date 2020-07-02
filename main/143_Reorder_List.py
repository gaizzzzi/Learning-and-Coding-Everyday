# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        
        self.node = head
        def helper(node):
            if node.next:
                helper(node.next)
            if not self.node:
                return
            if self.node == node or self.node.next == node:
                self.node = node.next = None
                return
            node.next, self.node.next = self.node.next, node 
            self.node = node.next
            
        helper(head)
        
# reduced adundant spaces
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        # find mid node as slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse what is after the mid node
        node = slow.next
        while node and node.next:
            nodenext, node.next = node.next, node.next.next
            nodenext.next, slow.next = slow.next, nodenext
            
        # insert reversed node in between first half
        fast = head
        while fast.next and slow.next:
            fastnext = fast.next
            fast.next, slow.next = slow.next, slow.next.next
            fast.next.next = fast = fastnext
        
        
        