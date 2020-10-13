class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        def helper(i, j):
            for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if -1 < ni < len(grid) and -1 < nj < len(grid[0]) and grid[ni][nj] == "1" and not (ni, nj) in visited:
                    visited.add((ni, nj))
                    helper(ni, nj)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i, j) in visited:
                    count += 1
                    helper(i, j)
        return count

