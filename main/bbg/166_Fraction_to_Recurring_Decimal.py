class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator ^ denominator) < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part = str(numerator // denominator)
        numerator %= denominator
        decimal_part = ""
        numerator_map = {} #{numerator: idx in decimal part}
        while numerator:
            decimal_digit = str(numerator * 10 // denominator)
            if numerator in numerator_map:
                return sign + integer_part + "." + decimal_part[:numerator_map[numerator]] + "(" + decimal_part[numerator_map[numerator]:] + ")"
            else:
                numerator_map[numerator] = len(decimal_part)
            decimal_part += decimal_digit
            numerator = numerator * 10 % denominator
            
        return sign + (integer_part + "." + decimal_part if decimal_part else integer_part)