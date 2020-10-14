# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse(head):
            pseudohead = ListNode(0, head)
            prev, curr = pseudohead, head
            length = 0
            while curr:
                length += 1
                currnext = curr.next
                curr.next = prev
                prev = curr
                curr = currnext
            head.next = None
            return (prev, length)
        
        (rev_l1, len_l1), (rev_l2, len_l2) = reverse(l1), reverse(l2)
        if len_l1 < len_l2:
            rev_l1, rev_l2 = rev_l2, rev_l1
        curr1, curr2 = rev_l1, rev_l2
        remainer = 0
        while curr1:
            val = curr1.val + remainer + (curr2.val if curr2 else 0)
            curr1.val = val % 10
            remainer = val // 10
            curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if remainer:
            return ListNode(1, reverse(rev_l1)[0])
        return reverse(rev_l1)[0]
            