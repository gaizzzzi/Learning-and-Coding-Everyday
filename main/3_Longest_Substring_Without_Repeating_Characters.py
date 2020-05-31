class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #14:58 - 15:08 hash + two pointers
        if not s:
            return 0
        start, end = 0, 0
        maxlength = 0
        letter_map = {}
        while end < len(s):
            if letter_map.get(s[end]) is not None:
            start = max(letter_map[s[end]] + 1, start)
            letter_map[s[end]] = end
            maxlength = max(maxlength, end - start + 1)
            end += 1
        return maxlength