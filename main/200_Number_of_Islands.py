class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = [[False]* len(grid[0]) for i in range(len(grid))]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs_helper(x, y):
            for (dx, dy) in directions:
                new_x, new_y =  x + dx, y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y]:
                    if grid[new_x][new_y] == '1':
                        visited[new_x][new_y] = True
                        dfs_helper(new_x, new_y)
                        
        island_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    island_num += 1
                    dfs_helper(i, j)
        
        return island_num