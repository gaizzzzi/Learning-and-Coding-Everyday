class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp 17:39 - 17:44
        if not matrix:
            return 0
        count = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        ans = 0
        for i in range(1, len(count)):
            for j in range(1, len(count[0])):
                tmp = min(count[i][j - 1], count[i - 1][j - 1], count[i - 1][j])
                if matrix[i - 1][j - 1] == "1":
                    count[i][j] = tmp + 1
                ans = max(count[i][j], ans)
        
        return ans ** 2