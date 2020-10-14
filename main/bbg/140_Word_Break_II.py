class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        def helper(s): # return all combinations of s
            res = [s] if s in wordSet else []
            for i in range(1, len(s)):
                # s[:i], s[i:]
                prefix = s[:i]
                suffix = s[i:]
                if prefix in wordSet:
                    if not suffix in memo:
                        memo[suffix] = helper(suffix)
                    if memo[suffix]:
                        res.extend([prefix + " " + suf for suf in memo[suffix]])
            return res
        memo[s] = helper(s)
        return memo[s]