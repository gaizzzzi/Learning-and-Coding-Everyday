class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = ""
        tmp = 0
        for i in range(-1, -max(len(num1), len(num2)) - 1, -1):
            n1 = ord(num1[i]) - ord("0") if -i < len(num1) + 1 else 0
            n2 = ord(num2[i]) - ord("0") if -i < len(num2) + 1 else 0
            ans = str((n1 + n2 + tmp) % 10) + ans
            tmp = (n1 + n2 + tmp) // 10
            
        if tmp:
            return "1" + ans
        
        return ans