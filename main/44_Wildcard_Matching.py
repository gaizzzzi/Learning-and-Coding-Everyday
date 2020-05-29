class Solution:
    def isMatch_dp(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not p:
            return False
        if not s:
            return list(set(p)) == ["*"]
        
        f = [[False] * len(s) for i in range(len(p))]
        if s[0] == p[0] or p[0] == "*" or p[0] == "?":
            f[0][0] = True
        for i in range(1, len(s)):
            if p[0] == "*":
                f[0][i] = True
            else:
                f[0][i] = False
        if_still_star = p[0] == "*"
        for i in range(1, len(p)):
            if p[i] == "*":
                f[i][0] = f[i - 1][0]
            elif if_still_star:
                f[i][0] = f[i - 1][0] and p[i] == s[0] or p[i] == "?"
                if_still_star = False
            
            else:
                f[i][0] = False
                
        if_last_unstar_match = f[0]
        abs_len = (p[0] != "*") - 1
        
        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if i == 3 and j == 1:
                    a = 1
                if p[i] == "*":
                    f[i][j] = f[i - 1][j - 1] or f[i - 1][j] or f[i][j - 1]
                else:
                    
                    if p[i] == "?":
                        f[i][j] = f[i - 1][j - 1] or if_last_unstar_match[j - 1] and j > abs_len 
                    else:
                        f[i][j] = (f[i - 1][j - 1] or if_last_unstar_match[j - 1]) and p[i] == s[j] and abs_len < j
            if p[i] != "*":
                abs_len += 1
                if_last_unstar_match = f[i]
        return f[len(p) - 1][len(s) - 1]