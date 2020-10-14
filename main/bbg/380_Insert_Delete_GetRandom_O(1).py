class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = [] #[val]
        self.val_map = {} #{val: idx in val_list}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_map:
            return False
        self.val_list.append(val)
        self.val_map[val] = len(self.val_list) - 1
        
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.val_map:
            return False
        self.val_list[self.val_map[val]] = self.val_list[-1]
        self.val_map[self.val_list[-1]] = self.val_map[val]
        self.val_list.pop()
        self.val_map.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_idx = int(random.random() * len(self.val_list))
        return self.val_list[random_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()