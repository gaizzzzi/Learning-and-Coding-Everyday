class Solution:
    def numDecodings(self, s: str) -> int:
        #dp 17:45-17:53
        if not s:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = int("0" < s[0] <= "9")
        for i in range(2, len(dp)):
            if "0" < s[i - 1] <= "9":
                dp[i] += dp[i - 1]
            if "09" < s[i - 2: i] < "27":
                dp[i] += dp[i - 2]
            if not dp[i]:
                return 0
        return dp[-1]
        