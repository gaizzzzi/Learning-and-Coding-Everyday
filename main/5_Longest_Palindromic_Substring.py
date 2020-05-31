class Solution:
    def longestPalindrome(self, s: str) -> str:
        #15:15 dp
        if not s:
            return s
        dp = [[False] * (len(s) + 2) for i in range(len(s))]
        for i in (0,1):
            for j in range(len(s)):
                dp[j][i] = True
        maxlen = 0
        maxsubstring = s[0]
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                dp[i][l] = dp[i + 1][l - 2] and s[i] == s[i + l - 1]
                if dp[i][l] and maxlen < l:
                    maxlen = l
                    maxsubstring = s[i: i + l]
        return maxsubstring