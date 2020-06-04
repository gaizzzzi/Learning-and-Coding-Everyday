class Solution:
    def uniquePaths_DP_On_2(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        dp[0] = 1
        for i in range(1, m):
            tmp = [1]
            for j in range(1, n):
                tmp.append(dp[j] + tmp[j - 1])
            dp = tmp
        return dp[-1]

    def uniquePaths_permutations_On(self, m: int, n: int) -> int:
        # c（m + n - 2, n - 1)
        m, n = max(m , n), min(m, n)
        ans = 1
        b = m
        for a in range(1, n):
            ans *=  b / a
            b += 1
        return round(ans)