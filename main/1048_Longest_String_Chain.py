class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        maxlong = 1
        dp = {word: 1 for word in words}
        for word in words:
            for k in range(len(word)):
                tmp = word[:k] + word[k + 1:]
                if tmp in dp:
                    dp[word] = max(dp[word], dp[tmp] + 1)
                    maxlong = max(maxlong, dp[word])
        return maxlong

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = len)
        maxlong = 1
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(i):
                if len(words[i]) == len(words[j]) + 1:
                    for k in range(len(words[i])):
                        if words[i][:k] == words[j][:k] and words[i][k + 1:] == words[j][k:]:
                            dp[i] = max(dp[i], dp[j] + 1)
                            maxlong = max(maxlong, dp[i])
        return maxlong