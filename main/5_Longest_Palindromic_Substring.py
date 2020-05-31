class Solution:
    def longestPalindrome_dp_3428ms(self, s: str) -> str:
        #15:15 dp
        if not s:
            return s
        dp = [[False] * (len(s) + 2) for i in range(len(s))]
        for i in (0,1):
            for j in range(len(s)):
                dp[j][i] = True
        maxlen = 0
        maxsubstring = s[0]
        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                dp[i][l] = dp[i + 1][l - 2] and s[i] == s[i + l - 1]
                if dp[i][l] and maxlen < l:
                    maxlen = l
                    maxsubstring = s[i: i + l]
        return maxsubstring

    def longestPalindrome_add_star_2596ms(self, s: str) -> str:
        s = "*" + "*".join(list(s)) + "*"
        maxlen = 0
        maxsubstring = ""
        for i in range(len(s)):
            l = 0
            while i + l < len(s) and i - l >= 0 and s[i - l] == s[i + l]:
                if l > maxlen:
                    maxlen = l
                    maxsubstring = s[i - l: i + l + 1]
                l += 1
        return maxsubstring.replace("*", "")

    def longestPalindrome_expand_in_two_ways_1280ms(self, s: str) -> str:
        maxlen = 0
        maxsubstring = ""
        for i in range(len(s)):
            l = 0
            while i + l < len(s) and i - l >= 0 and s[i - l] == s[i + l]:
                l += 1
            if 2 * l - 1 > maxlen:
                maxlen = 2 * l - 1
                maxsubstring = s[i - l + 1: i + l]
            l = 0
            while i + l + 1 < len(s) and i - l >= 0 and s[i - l] == s[i + 1 + l]:
                l += 1
            if 2 * l > maxlen:
                maxlen = 2 * l
                maxsubstring = s[i - l + 1: i + l + 1]
        return maxsubstring

    def longestPalindrome_expand_in_function_938ms(self, s: 'str') -> 'str':
        self.maxlen = 0
        self.longstr = ""
        
        def expand(s, l, r):
            while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                    l -= 1
                    r += 1

            if self.maxlen < r-l-1:
                self.maxlen = r-l-1
                self.longstr = s[l+1:r]
        
        for centre in range(len(s)):
            expand(s,centre,centre)
            expand(s,centre,centre+1)
        
        return self.longstr
            
    