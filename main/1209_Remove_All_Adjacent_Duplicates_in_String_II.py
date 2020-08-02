class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1][0]:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
            if stack and stack[-1][1] == k:
                stack.pop()
        return "".join([char * num for char, num in stack])