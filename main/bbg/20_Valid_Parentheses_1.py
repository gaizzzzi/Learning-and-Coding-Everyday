class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {"}": "{", ")": "(", "]": "["}
        for char in s:
            if char in char_map:
                if stack and stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False