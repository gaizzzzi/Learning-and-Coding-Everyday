class Solution:
    def decodeString(self, s: str) -> str:
        num_stack, str_stack = [], [] 
        curr_num, curr_str = "", ""
        for char in s:
            if char.isdigit():
                curr_num += char
            elif char == "[":
                num_stack.append(int(curr_num))
                str_stack.append(curr_str)
                curr_num, curr_str = "", ""
            elif char == "]":
                curr_str = num_stack.pop() * curr_str
                if str_stack:
                    curr_str = str_stack.pop() + curr_str
            else:
                curr_str += char
        return curr_str