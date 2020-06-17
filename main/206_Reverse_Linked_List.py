# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 17:32 - 17:36
        pre = None
        node = head
        while node:
            nodenext = node.next
            node.next = pre
            pre = node
            node = nodenext
        return pre