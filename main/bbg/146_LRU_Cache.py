class DBLLNode:
    def __init__(self, _val = 0, _prev = None, _next = None):
        self.val = _val
        self.prev = _prev
        self.next = _next

class LRUCache:
    def __init__(self, capacity):
        self.node_map = {}
        self.capacity = capacity
        self.head = DBLLNode()
        self.tail = DBLLNode()
        self.head.next, self.tail.prev = self.tail, self.head


    def get(self, key): # return value or -1
        if self.node_map.get(key) is None:
            return -1

        node = self.node_map[key]
        self.insert_before_tail(node)
        return node.val

    def insert_before_tail(self, node):
        self.tail.prev.next, node.prev = node, self.tail.prev
        node.next, self.tail.prev = self.tail, node

    def delete_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def put(self, key, value): # 
        # find/create the node 
        if self.node_map.get(key) is None:
            if len(self.node_map) >= self.capacity:
                self.delete_node(self.head.next)
            node = DBLLNode(value)
            self.node_map[key] = node
        else:
            node = self.node_map[key]
            self.delete_node(node)

        # put the node in the most recent place
        self.insert_before_tail(node)