class Solution:
    def multiply_time_wasted(self, num1: str, num2: str) -> str:
        # 15:36 - 16:38
        zero = ord("0")
        if len(num1) < len(num2):
            num1, num2 = num2, num1
            
        def add(num1, num2):
            if num2 == "0":
                return num1
            if not num1:
                return num2
            
            pre = "0"
            sum_ = ""
            if len(num1) < len(num2):
                num1, num2 = num2, num1
            i = -1
            while i > -len(num2) - 1:
                tmp = ord(pre) + ord(num1[i]) + ord(num2[i]) - 3 * zero 
                sum_ = str(tmp % 10) + sum_
                pre = str(tmp // 10)
                i -= 1
            return(add(num1[:i + 1], pre) + sum_)
                
        def mul(nums, digit):
            if digit == "0":
                return "0"
            pre = "0"
            prod = ""
            for num in nums[::-1]:
                tmp = ord(pre) - zero + (ord(num) - zero) * (ord(digit) - zero)
                prod = str(tmp % 10) + prod
                pre = str(tmp // 10)
            return (pre if pre != "0" else "") + prod
        
        prod = "0"
        count = 0
        for num in num2[::-1]:
            prod = add(mul(num1, num) + "0" * count, prod)
            count += 1
        
        return prod


    def multiply_optimized(self, num1: str, num2: str) -> str:
        # 16:44 - 17:01
        ans = [0] * (len(num1) + len(num2))
        pos = len(ans) - 1
        for n1 in num1[::-1]:
            tmp_pos = pos
            for n2 in num2[::-1]:
                ans[tmp_pos] += int(n1) * int(n2)
                ans[tmp_pos - 1] += ans[tmp_pos] // 10
                ans[tmp_pos] %= 10
                tmp_pos -= 1
            pos -= 1
        pos = 0
        while pos < len(ans) - 1 and ans[pos] == 0:
            pos += 1
        return "".join(map(str, ans[pos:]))