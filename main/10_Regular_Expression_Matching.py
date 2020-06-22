class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        pp = []
        i = -1
        for char in p:
            if char == "*":
                pp[i] += "*"
            else:
                pp.append(char)
                i += 1

        #print(pp)          
        dp = [[False] * (len(pp) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(pp) + 1):
            dp[0][i] = dp[0][i - 1] and ("*" in pp[i - 1])
            
        for i in range(1, len(s) + 1):
            for j in range(1, len(pp) + 1):
                dp[i][j] = (dp[i - 1][j - 1] and (s[i - 1] in pp[j - 1] or "." in pp[j - 1])) or \
                           (dp[i - 1][j] and (pp[j - 1] == s[i - 1] + "*" or pp[j - 1] == ".*")) or \
                           (dp[i][j - 1] and ("*" in pp[j - 1]))
       
        #print(dp)
        return dp[-1][-1]