class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # 20:21 - 20:55
        if not s:
            return 0
        start, end, tmp_start, maxlen = 0, 1, 0, 0
        letters = [s[0]]
        while end < len(s):
            if s[end] != s[end - 1]:
                if len(letters) == 2:
                    if not s[end] in letters:
                        maxlen = max(maxlen, end - start)
                        start = tmp_start
                    letters.pop(0)
                letters.append(s[end])  
                tmp_start = end
            end += 1
        maxlen = max(maxlen, end - start)
        return maxlen