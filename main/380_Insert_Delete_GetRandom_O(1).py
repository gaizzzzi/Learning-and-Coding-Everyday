class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_set = {}
        self.list_helper = [-1]
        self.count = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
       #print(self.random_set.get(val))
        if self.random_set.get(val) != None:
            return False
        
        self.random_set[val] = self.count
        self.list_helper[self.count] = val
        self.count += 1
        self.list_helper.append(-1)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if not val in self.random_set:
            return False
        
        self.list_helper[self.random_set[val]] = self.list_helper[self.count - 1]
        self.random_set[self.list_helper[self.count - 1]] = self.random_set[val]
        del self.random_set[val]
        self.count -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_factor = int(random.random() * self.count)
        return(self.list_helper[random_factor])


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()