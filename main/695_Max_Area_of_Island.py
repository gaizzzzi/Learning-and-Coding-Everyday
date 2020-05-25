class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs_helper(x, y, areas):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y] and grid[x][y] == 1:
                visited[x][y] = True
                areas[0] += 1
                areas[1] = max(areas[0], areas[1])
                
                for (dx, dy) in directions:
                    new_x, new_y = x + dx, y + dy
                    dfs_helper(new_x, new_y, areas)
        areas = [0, 0]         
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    areas[0] = 0
                    dfs_helper(i, j, areas)
        
        return areas[1]
    