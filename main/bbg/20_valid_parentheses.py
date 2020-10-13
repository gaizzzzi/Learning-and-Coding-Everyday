def isValid(self, s: str) -> bool:
    stack = []
    prt_map = {")":"(", "}":"{", "]":"["}
    for char in s:
        if char in "([{":
            stack.append(char)
        else: 
            if stack and stack[-1] == prt_map[char]:
                stack.pop()
            else:
                return False
    return stack == []