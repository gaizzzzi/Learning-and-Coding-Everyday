# test case is small n * m <= 20 
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.ans = 0
        
        def helper(_x, _y, visited, depth):
            if grid[_x][_y] == 2:
                    self.ans += int(depth == self.empty + 1)
                    return
            
            for dx, dy in directions:
                x, y = _x + dx, _y + dy
                if -1 < x < len(grid) and -1 < y < len(grid[0]):
                    tmp = 1 << (x * len(grid[0]) + y)
                    if grid[x][y] in [0, 2] and not visited & tmp:
                        helper(x, y, visited | tmp, depth + 1)
        
        self.empty = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                if not grid[i][j]:
                    self.empty += 1
                    
        helper(x, y, 0, 0) # x, y, visited, depth
        return self.ans
                    