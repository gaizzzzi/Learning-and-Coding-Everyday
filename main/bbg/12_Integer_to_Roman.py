class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        roman_list = ["M", "D", "C", "L", "X", "V", "I"]
        ans, roman_idx, divisor = "", 0, 1000
        while num:
            quotient = num // divisor
            num %= divisor
            #print(quotient, num, divisor, roman_idx, divisor, roman_list[roman_idx])
            if not roman_idx % 2: # divisor == 500 or 50 or 5
                if quotient == 4:
                    if ans and ans[-1] == roman_list[roman_idx - 1]:
                        ans = ans[:-1] + roman_list[roman_idx] + roman_list[roman_idx - 2]
                    else:
                        ans += roman_list[roman_idx] + roman_list[roman_idx - 1]
                else:
                    ans += roman_list[roman_idx] * quotient
                divisor //= 2
            else: # divisor == 1000 or 100 or 10 or 1
                ans += roman_list[roman_idx] * quotient
                divisor //= 5
            roman_idx += 1
        return ans