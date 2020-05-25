class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs_helper(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 1:
                visited[x][y] = True
                area = 1
                for (dx, dy) in directions:
                    new_x, new_y = x + dx, y + dy
                    area += dfs_helper(new_x, new_y)
                return area
            else:
                return 0

        max_area = 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    
                    max_area = max(max_area, dfs_helper(i, j))
                    
        return max_area
