class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        
        def dfs_helper(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 1:
                visited[x][y] = True
                return(dfs_helper(x - 1, y)
                    + dfs_helper(x + 1, y)
                    + dfs_helper(x, y - 1)
                    + dfs_helper(x, y + 1)
                    + 1)
            return 0

        max_area = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, dfs_helper(i, j))
                    
        return max_area
