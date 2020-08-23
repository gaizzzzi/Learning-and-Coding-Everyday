class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = collections.Counter(s)
        for i, char in enumerate(s):
            if s_counter[char] == 1:
                return i
        return -1