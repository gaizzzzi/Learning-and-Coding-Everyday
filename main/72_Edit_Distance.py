class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp
        # 18:20 - 18:52
        dp = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]
        dp[0] = [i for i in range(len(word1) + 1)]
        for i in range(1, len(word2) + 1):
            dp[i][0] = i
            for j in range(1, len(word1) + 1):
                if_match = int(word1[j - 1] == word2[i - 1])
                dp[i][j] = min(dp[i - 1][j - 1] - if_match, dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]