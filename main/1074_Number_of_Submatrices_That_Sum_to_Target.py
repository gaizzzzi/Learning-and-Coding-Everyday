class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = pre_sum[i][j - 1] + pre_sum[i - 1][j] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        ans = 0
        for x1 in range(1, m + 1):
            for x2 in range(x1):
                num_map = defaultdict(int)
                num_map[0] = 1
                cum_sum = 0
                for y in range(1, n + 1):
                    cum_sum = pre_sum[x1][y] - pre_sum[x2][y]
                    ans += num_map[cum_sum - target]
                    num_map[cum_sum] += 1
                    

        return ans