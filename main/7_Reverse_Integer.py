class Solution:
    def reverse(self, x: int) -> int:
        # 19:50 - 20:00
        maxint = str(1 << 32 - 1)
        minint = str(-(1 << 31))
        str_x = str(x)
        if str_x[0] == "-":
            str_x = "-" + str_x[1:][::-1]
            if len(str_x) < 11 or (len(str_x) == 11 and str_x <= minint):
                return int(str_x)
        else:
            str_x = str_x[::-1]
            if len(str_x) < 10 or (len(str_x) == 10 and str_x <= maxint):
                return int(str_x)
        return 0