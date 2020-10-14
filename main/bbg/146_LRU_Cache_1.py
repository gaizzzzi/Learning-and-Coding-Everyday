class DoubleNode:
    def __init__(self, key = 0, value = 0, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.aval_size = capacity
        self.key_map = {} #key, node
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def insert_before_tail(self, node):
        node.next, node.prev = self.tail, self.tail.prev
        self.tail.prev.next, self.tail.prev = node, node
        
    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def update_to_recent(self, node):
        self.delete_node(node)
        self.insert_before_tail(node)
    
    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.update_to_recent(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self.update_to_recent(node)
        else:
            node = DoubleNode(key, value)
            self.key_map[key] = node
            self.insert_before_tail(node)
            if self.aval_size == 0:
                self.key_map.pop(self.head.next.key)
                self.delete_node(self.head.next)
            else:
                self.aval_size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)