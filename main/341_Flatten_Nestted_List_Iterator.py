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
        self.nested_list_stack = nestedList[::-1]
    def next(self) -> int:
        return self.current_nested_list.getInteger()
        
    def hasNext(self) -> bool:
        while self.nested_list_stack:
            self.current_nested_list = self.nested_list_stack.pop()
            if self.current_nested_list.isInteger():
                return True
            else:
                self.nested_list_stack.extend(self.current_nested_list.getList()[::-1])
        return False



        # while self.current_pos_stack:
        #     while self.current_pos_stack and self.current_pos_stack[-1] + 1 > len(self.nested_list_stack[-1]) - 1:
        #         self.current_pos_stack.pop()
        #         self.nested_list_stack.pop()
                    
        #     if not self.current_pos_stack:
        #         return False
            
        #     self.current_pos_stack[-1] += 1
        #     self.current_pos = self.nested_list_stack[-1][self.current_pos_stack[-1]]
        
        #     if self.current_pos.isInteger():
        #         return True
                
        #     else:
        #         self.nested_list_stack.append(self.current_pos.getList())
        #         self.current_pos_stack.append(-1)
                
        # return False
            

    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())