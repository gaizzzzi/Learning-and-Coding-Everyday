class Solution:
    def calculate(self, s: str) -> int:
        stack_num = []
        pre_sign = "+"
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            if "0" <= s[i] <= "9":
                tmp = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    tmp = tmp * 10 + ord(s[i]) - ord("0")
                    i += 1
                if pre_sign == "+":
                    stack_num.append(tmp)
                elif pre_sign == "-":
                    stack_num.append(-tmp)
                elif pre_sign == "*":
                    stack_num.append(stack_num.pop() * tmp)
                else:
                    last_num = stack_num.pop()
                    if last_num < 0:
                        stack_num.append(-(abs(last_num) // tmp))
                    else:
                        stack_num.append(last_num // tmp)
            else:
                pre_sign = s[i]
                i += 1
        return sum(stack_num)
