class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        stack_sign = [1]
        ans = 0
        pre_sign = 1
        while i < len(s):
            paren_flag = 1    
            if s[i] == " ":
                i += 1
                continue
            elif "0" <= s[i] <= "9":
                tmp = 0
                while i < len(s) and "0" <= s[i] <= "9":
                    tmp = tmp * 10 + ord(s[i]) - ord("0")
                    i += 1
                ans += pre_sign * tmp * stack_sign[-1]
            elif s[i] == "-":
                pre_sign = -1
                i += 1
            elif s[i] == "+":
                pre_sign = 1
                i += 1
            elif s[i] =="(":
                stack_sign.append(pre_sign * stack_sign[-1])
                pre_sign = 1
                i += 1
            else:
                stack_sign.pop()
                i += 1
        return ans
            
                
            
                