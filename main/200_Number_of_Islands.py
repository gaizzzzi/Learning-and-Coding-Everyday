class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        width = len(grid)
        length = len(grid[0])
        
        visited = []
        for i in range(width):
            tmp = [False for j in range(length)]
            visited.append(tmp)
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs_helper(pos):
            for direc in directions:
                new_pos = [pos[0] + direc[0], pos[1] + direc[1]]
                if 0 <= new_pos[0] < width and 0 <= new_pos[1] < length and not visited[new_pos[0]][new_pos[1]]:
                    if grid[new_pos[0]][new_pos[1]] == '1':
                        visited[new_pos[0]][new_pos[1]] = True
                        dfs_helper(new_pos)
                        
        island_num = 0
        for i in range(width):
            for j in range(length):
                if grid[i][j] == '1' and not visited[i][j]:
                    island_num += 1
                    dfs_helper([i, j])
        
        return island_num