# kmp
class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        next = [-1] + [0] * (len(needle) - 1)
        i, j = 0, -1
        while i < len(needle) - 1:
            if j == -1 or needle[j] == needle[i]:
                j += 1
                i += 1
                next[i] = j
            else:
                j = next[j]
        
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                j = next[j]
        if j < len(needle):
            return -1
        
        return i - j
            