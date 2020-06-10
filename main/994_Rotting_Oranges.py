
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 20:46 - 21:01
        queue = []
        orange_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j]:
                    orange_count += 1
                    
        # one queue + two pointers          
        i, j = 0, len(queue)
        depth = 0
        while i < len(queue):
            if i == j:
                depth += 1
                j = len(queue)
            x , y = queue[i]
            visited[x][y] = True
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]):
                    if visited[new_x][new_y] or grid[new_x][new_y] != 1:
                        continue
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
            i += 1
            
        if len(queue) < orange_count:
            return -1
        return depth
        