class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, maxlen = 0, 0, 0
        char_map = {} #{char: latest_idx}
        while end < len(s):
            if s[end] in char_map:
                start = max(char_map[s[end]] + 1, start)
            maxlen = max(end - start + 1, maxlen)
            char_map[s[end]] = end
            end += 1
        return maxlen