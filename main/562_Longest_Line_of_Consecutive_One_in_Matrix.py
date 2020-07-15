class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        dp = defaultdict(list)
        directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]
        maxlen = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    for idx, (di, dj) in enumerate(directions):
                        if (i + di, j + dj) in dp:
                            dp[(i, j)].append(dp[(i + di, j + dj)][idx] + 1)
                        else:
                            dp[(i, j)].append(1)
                        maxlen = max(maxlen, dp[(i, j)][-1])
        
        return maxlen