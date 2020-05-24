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
        self.nested_list = nestedList
        self.position = -1
        
        def next_helper(nested_list, flattened_list):
            
            if nested_list.isInteger():
                flattened_list.append(nested_list.getInteger())
                
            child_nested_list = nested_list.getList()
            
            if child_nested_list:
                for item in child_nested_list:
                    next_helper(item, flattened_list)

        self.flattened_list = []
        for item in self.nested_list:
            next_helper(item, self.flattened_list)
        
            
    def next(self) -> int:
        return self.flattened_list[self.position]
    
    def hasNext(self) -> bool:
        self.position += 1
        return self.position < len(self.flattened_list)
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())