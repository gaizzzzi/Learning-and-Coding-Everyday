# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddhead, evenhead, node = ListNode(0), ListNode(0), head
        even, odd = evenhead, oddhead
        i = 0
        while node:
            if i & 1:
                even.next = node
                even = even.next
            else:
                odd.next = node
                odd = odd.next
            node = node.next
            i += 1
        even.next = None
        odd.next = evenhead.next
            
        return oddhead.next
            