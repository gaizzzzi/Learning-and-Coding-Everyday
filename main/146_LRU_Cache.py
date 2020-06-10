class node:
    def __init__(self, key = 0, value = 0, _prev = None, _next = None):
        self.key = key
        self.value = value
        self.prev = _prev
        self.next = _next
        
class LRUCache:
    # 21:35 - 22:00
    # hash + double linked list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.size = 0
        self.head = node(0)
        self.tail = node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.map:
            self._remove_current(key)
            self._update_tail(key)
            return self.map[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self._remove_current(key)
            
        else:
            if self.size == self.capacity:
                self._delete()
            else:
                self.size += 1
            self.map[key] = node(key, value)
        self._update_tail(key)
    
    def _remove_current(self, key):
        self.map[key].next.prev = self.map[key].prev
        self.map[key].prev.next = self.map[key].next
    
    def _update_tail(self, key):
        self.map[key].prev = self.tail.prev
        self.tail.prev.next = self.map[key]
        self.tail.prev = self.map[key]
        self.map[key].next = self.tail
    
    def _delete(self):
        _map = self.head.next
        del self.map[_map.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)