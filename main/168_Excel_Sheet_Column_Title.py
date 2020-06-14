class Solution:
    def convertToTitle(self, n: int) -> str:
        # 26 进制
        # 00:40 - 00:56
        ans = ""
        n -= 1
        while n >= 0:
            ans = chr(n % 26 + ord("A")) + ans
            n = n // 26 - 1
        return ans