# method 1: one double linked list + 3 maps
class dllink:
    def __init__(self, _value = 1, _count = 1, _prev = None, _next = None):
        self.value = _value
        self.count = _count
        self.prev = _prev
        self.next = _next
        
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_map = {}
        self.value_map = {0: {""}}
        self.head, self.tail = dllink(0, 0), dllink(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.value_link = {0: self.head}
        
    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def add(self, node1, node2):
        node2.next, node2.prev = node1.next, node1
        node1.next, node2.next.prev = node2, node2
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key_map:
            self.value_map[self.key_map[key]].remove(key)
            
        self.key_map[key] = self.key_map.get(key, 0) + 1
        
        if not self.key_map[key] in self.value_map:
            self.value_map[self.key_map[key]] = {key}
        else:
             self.value_map[self.key_map[key]].add(key)
                
        # deal with new value       
        if not self.value_link.get(self.key_map[key]):
            node = dllink(self.key_map[key])
            self.value_link[self.key_map[key]] = node
            self.add(self.value_link[self.key_map[key] - 1], node)
        else:
            node = self.value_link[self.key_map[key]]
            node.count += 1
            
        # deal with old value
        if self.key_map[key] - 1:
            self.value_link[self.key_map[key] - 1].count -= 1
            if not self.value_link[self.key_map[key] - 1].count:
                self.delete(self.value_link[self.key_map[key] - 1])
                self.value_link.pop(self.key_map[key] - 1)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if not self.key_map.get(key, 0):
            return
        
        self.value_map[self.key_map[key]].remove(key)
        old_node = self.value_link.get(self.key_map[key])
                                   
        if self.key_map.get(key) == 1:
            self.key_map.pop(key)
        else:
            self.key_map[key] -= 1
            self.value_map[self.key_map[key]].add(key)
        
        # deal with new value
        if self.key_map.get(key):
            if not self.value_link.get(self.key_map[key]):
                node = dllink(self.key_map[key])
                self.value_link[self.key_map[key]] = node
                self.add(self.value_link[self.key_map[key] + 1].prev, node)
                
            else:
                node = self.value_link[self.key_map[key]]
                node.count += 1
        
        # deal with old value
        old_node.count -= 1
        if not old_node.count:
            self.delete(old_node)
            self.value_link.pop(old_node.value)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        tmp = self.value_map[self.tail.prev.value].pop()
        self.value_map[self.tail.prev.value].add(tmp)
        return tmp

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        tmp = self.value_map[self.head.next.value].pop()
        self.value_map[self.head.next.value].add(tmp)
        return tmp


# method 2: 1 linked list + 1 map
# 19:12 - 19:36
class dllist:
    def __init__(self, _key = {""}, _value = 1, _prev = None, _next = None):
        self.key = _key
        self.value = _value
        self.prev = _prev
        self.next = _next
        
class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head, self.tail = dllist({""}, 0), dllist({""}, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.key_map = {}

    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    def add(self, node1, node2):
        node2.next, node2.prev = node1.next, node1
        node1.next, node2.next.prev = node2, node2
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        node = self.key_map.get(key, self.head)
        
        # deal with new node
        if node.next.value == node.value + 1:
            node.next.key.add(key)
        else:
            next_node = dllist({key}, node.value + 1)
            self.add(node, next_node)
        
        # deal with old node
        if node.value:
            node.key.remove(key)
            if not node.key:
                self.delete(node)
                
        self.key_map[key] = node.next
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if not key in self.key_map:
            return
        node = self.key_map[key]
        
        # deal with new node
        if node.value - 1:
            if node.value - 1 == node.prev.value:
                node.prev.key.add(key)
            else:
                prev_node = dllist({key}, node.value - 1)
                self.add(node.prev, prev_node)
                
            self.key_map[key] = node.prev
        else:
            self.key_map.pop(key)
        
        # deal with old node
        node.key.remove(key)
        if not node.key:
            self.delete(node)
        
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        tmp = self.tail.prev.key.pop()
        self.tail.prev.key.add(tmp)
        return tmp
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        tmp = self.head.next.key.pop()
        self.head.next.key.add(tmp)
        return tmp