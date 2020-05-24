# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.position = -1
        
        def next_helper(nested_list): 
            if not nested_list:
                return
            for item in nested_list:
                if item.isInteger():
                    self.flattened_list.append(item.getInteger()) 
                else:
                    child_nested_list = item.getList()
                    next_helper(child_nested_list)

        self.flattened_list = []
        
        next_helper(nestedList)
        
            
    def next(self) -> int:
        return self.flattened_list[self.position]
    
    def hasNext(self) -> bool:
        self.position += 1
        return self.position < len(self.flattened_list)
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())