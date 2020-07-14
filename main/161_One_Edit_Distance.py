class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        i = 0
        while i < len(s) and s[i] == t[i]:
            i += 1
        return not i == len(s) == len(t) and \
            any([s[i:] == t[i + 1:], s[i + 1:] == t[i + 1:]])