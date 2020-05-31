class Solution:
    def isMatch_dp(self, s: str, p: str) -> bool:
        f = [[False] * (len(s) + 1) for i in range(len(p) + 1)] # included null string
        f[0][0] = True # "" == ""

        for i in range(1, len(p) + 1):
            f[i][0] == f[i - 1][0] and p[i] == "*"
                
        abs_len = (p[0] != "*") - 1
        
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i] == "*":
                    f[i][j] = f[i - 1][j - 1] or f[i - 1][j] or f[i][j - 1]
                else:
                    if p[i] == "?":
                        f[i][j] = j > abs_len and (f[i - 1][j - 1] or (f[i - 1][j] and (i > 1 and p[i - 2] == "*" or i < 2)))
                    else:
                        f[i][j] = j > abs_len and (f[i - 1][j - 1] or (f[i - 1][j] and (i > 1 and p[i - 2] == "*" or i < 2))) and p[i - 1] == s[j - 1]
            if p[i] != "*":
                abs_len += 1

        return f[-1][-1]
