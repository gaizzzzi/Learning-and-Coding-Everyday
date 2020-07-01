class Solution:
    def wordBreak_divid_and_conquer_timeout(self, s: str, wordDict: List[str]) -> bool:
        # divid&conquer
        word_map = set(wordDict)
        def helper(s):
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                if prefix in word_map and suffix in word_map:
                    return True
                if prefix in word_map and helper(suffix):
                    return True
            return False
        return s in word_map or helper(s)

    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        # dp
        word_map = {}
        for word in wordDict:
            if not len(word) in word_map:
                word_map[len(word)] = {word}
            else:
                word_map[len(word)].add(word)
            
        dp = [True] + [False] * len(s)
        for i in range(len(dp)):
            for j in sorted(word_map.keys()):
                if i + j >= len(dp):
                    break
                dp[i + j] |= dp[i] and (s[i:i + j] in word_map[j])
        return dp[-1]