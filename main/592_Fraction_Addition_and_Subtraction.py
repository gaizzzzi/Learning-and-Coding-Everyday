class Solution:
    def fractionAddition(self, expression: str) -> str:
        def greatest_common_divisor(n1, n2):
            while n2:
                n1, n2 = n2, n1 % n2
            return n1
        def fraction_add(frac1, frac2):
            gcd = greatest_common_divisor(frac1[1], frac2[1])
            divisor = frac1[1] // gcd * frac2[1]
            dividend = divisor // frac2[1] * frac2[0] + divisor // frac1[1] * frac1[0]
            gcd = greatest_common_divisor(abs(dividend), divisor)
            return [dividend // gcd, divisor // gcd]
            
        expr = split(expression, "+-")
        is_plus, tmp, result = 1, "", [0, 1]
        divisor, dividend = 1, 0
        for char in expression:
            if char in "+-":
                is_plus = 1 if char == "+" else -1
                if tmp:
                    divisor = int(tmp)
                    tmp = ""
                    result = fraction_add(result, [dividend, divisor])
                    # these two results are similar, the one below is faster
                    # result = [result[0] * divisor + result[1] * dividend, divisor * result[1]]
            elif char == "/":
                dividend = is_plus * int(tmp)
                tmp = ""
            else:
                tmp += char
            if tmp:
                divisor = int(tmp)
        return "/".join(map(str, fraction_add(result, [dividend, divisor])))