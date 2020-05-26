class Solution:
    def mergeKLists_divide_and_conquer(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            if not lists[0]:
                return lists[1]
            if not lists[1]:
                return lists[0]
            if lists[0].val > lists[1].val:
                lists[0], lists[1] = lists[1], lists[0]
            lists[0].next = self.mergeKLists([lists[0].next, lists[1]])
            return lists[0]

        if len(lists) > 2:
            return self.mergeKLists([self.mergeKLists(lists[:len(lists)//2 + 1]),
                          self.mergeKLists(lists[len(lists)//2 + 1:])])
        return self.mergeKLists(lists)

    def mergeKLists_heap(self, lists: List[ListNode]) -> ListNode:
        hp = []
        count = 0 
        # adding count for each item in heap becomes unique - 
        # making sure when value is the same, heap don't compare 
        # next uncomparable variable "node"
        for node in lists:
            if node:
                heappush(hp, (node.val, count, node))
                count += 1
        
        current = head = ListNode(0)
        
        while hp:
            count += 1
            min_val, tmp, min_node  = heappop(hp)
            if min_node:
                current.next = min_node
                current = current.next
            if min_node.next:
                heappush(hp, (min_node.next.val, count, min_node.next))
        current.next = None
        
        return head.next
    