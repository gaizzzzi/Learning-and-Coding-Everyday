class Solution:
    def minPathSum_DP2D_beat_36(self, grid: List[List[int]]) -> int:
        # 22:11 - 22:15 
        # dp
        f = [[float("inf")] * (len(grid[0]) + 1) for i in range(len(grid) + 1)]
        f[0][1] = 0
        for i in range(1, len(grid) + 1):
            for j in range(1, len(grid[0]) + 1):
                print(i, j)
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i - 1][j - 1]
        return f[-1][-1]


    def minPathSum_DP1D_beat_92(self, grid: List[List[int]]) -> int:
        #22:20 - 22: 25
        dp = [float('inf')] * len(grid[0])
        dp[0] = 0
        for i in range(0,len(grid)):
            tmp = [grid[i][0] + dp[0]]
            for j in range(1,len(grid[0])):
                tmp.append(min(dp[j], tmp[j - 1]) + grid[i][j])
            dp = tmp
       	return dp[-1]