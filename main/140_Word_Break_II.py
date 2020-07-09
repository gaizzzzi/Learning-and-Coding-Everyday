class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_map = set(wordDict)
        memo = defaultdict(list)
        def helper(s):
            tmp = [s] if s in word_map else []
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                suffix_comb = []
                if prefix in word_map:
                    if suffix in memo:
                        suffix_comb = memo[suffix]
                    else:
                        suffix_comb.extend(helper(suffix))
                    tmp.extend([prefix + " " + y for y in suffix_comb])
            memo[s] = tmp
            return tmp
        return helper(s)