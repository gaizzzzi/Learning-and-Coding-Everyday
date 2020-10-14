class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        left_stack = [] # idx of "(" if not offset by ")"
        right_stack = []
        for idx, char in enumerate(s):
            if char == "(":
                left_stack.append(idx)
            elif char == ")":
                if left_stack:
                    left_stack.pop()
                else:
                    right_stack.append(idx)
        for idx in left_stack[::-1] + right_stack[::-1]:
            s.pop(idx)
        return "".join(s)
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, curr = [], ""
        for char in s:
            if char == "(":
                stack.append(curr)
                curr = ""
            elif char == ")":
                if stack:
                    curr = stack.pop() + "(" + curr + ")"
            else:
                curr += char
        return "".join(stack) + curr