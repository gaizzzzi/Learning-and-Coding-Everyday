# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers_reverse(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            node, prev = head, None
            while node:
                nodenext, node.next = node.next, prev
                prev, node = node, nodenext
            return prev
        
        rev1, rev2 = reverse(l1), reverse(l2)
        node1, node2, carry, prev = rev1, rev2, 0, None
        while node1 or node2:
            if not node1 and node2:
                prev.next, node1, node2 = node2, node2, None
            val2 = node2.val if node2 else 0
            tmp = node1.val + val2 + carry
            carry, node1.val = tmp // 10, tmp % 10
            prev, node1 = node1, node1.next
            if node2:
                node2 = node2.next
        if carry:
            prev.next = ListNode(1)
        
        return reverse(rev1)


class Solution:
    def addTwoNumbers_stack_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.stack1 = []
        while l1:
            self.stack1.append(l1.val)
            l1 = l1.next
        self.carry = 0
        
        def helper(node):
            if not node:
                return None
            node.next = helper(node.next)
            tmp = (self.stack1.pop() if self.stack1 else 0) + node.val + self.carry
            self.carry, node.val = tmp // 10, tmp % 10
            return node
        
        tail = helper(l2)
        while self.stack1 or self.carry:
            tmp = (self.stack1.pop() if self.stack1 else 0) + self.carry
            self.carry, node = tmp // 10, ListNode(tmp % 10, tail)
            tail = node
        
        return tail
        
                
        
                