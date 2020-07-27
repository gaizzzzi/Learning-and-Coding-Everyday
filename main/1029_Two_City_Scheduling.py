class Solution:
    def twoCitySchedCost_2d_dp(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        dp = [[float('inf')] * (n + 1) for _ in range(2 * n + 1)]
        dp[0][0] = 0
        for i in range(1, 2 * n + 1):
            dp[i][0] = costs[i - 1][1] + dp[i - 1][0]
        for i in range(1, 2 * n + 1):
            for j in range(max(1, i - n), min(i + 1, n + 1)):
                dp[i][j] = min(dp[i - 1][j - 1] + costs[i - 1][0], 
                              dp[i - 1][j] + costs[i - 1][1])
        return dp[-1][-1]

class Solution:
    def twoCitySchedCost_1d_dp(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        dp = costs[0] + [float('inf')] * (n - 1)
        for i in range(1, 2 * n):
            for j in range(min(i + 1, n), max(0, i - n - 1), -1):
                dp[j] = min(dp[j - 1] + costs[i][1], 
                            dp[j] + costs[i][0])
            dp[0] += costs[i][0]
        return dp[-1]

class Solution:
    def twoCitySchedCost_greedy(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0] - x[1])
        total = 0
        for i in range(len(costs) // 2):
            total += costs[i][0] + costs[i + len(costs) // 2][1]
        return total