class Solution:
    def numberToWords(self, num: int) -> str:
        # one pass
        if num == 0:
            return "Zero"
        forth_digit = ["Thousand", "Million", "Billion"]
        second_digit = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        two_digits = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        single_digit = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        
        ans = []
        digit_3 = -1
        while num:
            tmp_ans = []
            tmp_num = num % 1000
            hundred = tmp_num // 100
            if hundred:
                tmp_ans.extend([single_digit[hundred - 1], "Hundred"])
            tmp_num %= 100
            if 0 < tmp_num < 10:
                tmp_ans.extend([single_digit[tmp_num - 1]])
            elif 10 <= tmp_num < 20:
                tmp_ans.extend([two_digits[tmp_num - 10]])
            elif tmp_num:
                digit_2 = tmp_num // 10
                digit_1 = tmp_num % 10
                tmp_ans.append(second_digit[digit_2 - 2])
                if digit_1:
                    tmp_ans.append(single_digit[digit_1 - 1])
            if num and tmp_ans and digit_3 > -1:
                ans = [forth_digit[digit_3]] + ans
            ans = tmp_ans + ans
            digit_3 += 1
            num //= 1000
            
        return " ".join(ans)