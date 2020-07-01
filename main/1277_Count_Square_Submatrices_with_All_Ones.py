class Solution:
    def countSquares_BF_on3_timeout(self, matrix: List[List[int]]) -> int:
        # 17:02 - 17:12
        #print(len(matrix[0]))
        pre_sum = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(pre_sum)):
            for j in range(1, len(pre_sum[0])):
                pre_sum[i][j] = pre_sum[i][j - 1] + pre_sum[i - 1][j] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1]
        
        ans = 0
        for l in range(1, min(len(matrix), len(matrix[0])) + 1):
            #print(l)
            for row1 in range(len(pre_sum) - l):
                row2 = row1 + l
                for col1 in range(len(pre_sum[0]) - l):
                    col2 = col1 + l
                    if pre_sum[row2][col2] - pre_sum[row1][col2] - pre_sum[row2][col1] + pre_sum[row1][col1] == l * l:
                        ans += 1
        
        return ans
class Solution:
    def countSquares_on2(self, matrix: List[List[int]]) -> int:
        # dp 17:25 - 17:31
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0 and matrix[i][j]:
                    tmp = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                    if tmp:
                        matrix[i][j] = tmp + 1
                ans += matrix[i][j]
        return ans