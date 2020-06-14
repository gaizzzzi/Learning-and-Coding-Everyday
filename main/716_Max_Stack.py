class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.maxstack:
            self.maxstack.append(max(self.maxstack[-1], x))
        else:
            self.maxstack.append(x)

    def pop(self) -> int:
        self.maxstack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxstack[-1]

    def popMax(self) -> int:
        tmp = []
        maxvalue = self.maxstack[-1]
        while self.stack[-1] != maxvalue:
            tmp.append(self.stack.pop())
            self.maxstack.pop()
        self.stack.pop()
        self.maxstack.pop()
        for x in tmp[::-1]:
            self.push(x)
        return maxvalue
        

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()