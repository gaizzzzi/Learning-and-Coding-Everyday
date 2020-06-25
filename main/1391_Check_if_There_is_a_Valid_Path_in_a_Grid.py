class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        visited = set()
        
        def helper(prestep, x, y, last_x, last_y):
            if last_x == len(grid) - 1 and last_y == len(grid[0]) - 1:
                return True
            if not (-1 < x < len(grid) and -1 < y < len(grid[0])) or x * len(grid[0]) + y in visited:
                return False

            visited.add(x * len(grid[0]) + y)
            
            if grid[x][y] == 1:
                if prestep in [None, "right"]:
                    return helper("right", x, y + 1, x, y)
                elif prestep == "left":
                    return helper("left", x, y - 1, x, y)

            elif grid[x][y] == 2:
                if prestep in [None,"down"]:
                    return helper("down", x + 1, y, x, y)
                elif prestep ==  "up":
                    return helper("up", x - 1, y, x, y)
            
            elif grid[x][y] == 3:
                if prestep in [None, "right"]:
                    return helper("down", x + 1, y, x, y)
                elif prestep == "up":
                    return helper("left", x, y - 1, x, y)
            
            elif grid[x][y] == 4:
                if prestep == None:
                    return helper("right", x, y + 1, x, y) or helper("down", x + 1, y, x, y)
                elif prestep == "up":
                    return helper("right", x, y + 1, x, y)
                elif prestep == "left":
                    return helper("down", x + 1, y, x, y)
            
            elif grid[x][y] == 5:
                if prestep in [None, "down"]:
                    return helper("left", x, y - 1, x, y)
                elif prestep == "right":
                    return helper("up", x - 1, y, x, y)
            
            elif grid[x][y] == 6:
                if prestep in [None, "down"]:
                    return helper("right", x, y + 1, x, y)
                elif prestep == "right":
                    return helper("up", x - 1, y, x, y)
            
            return False
                
        return helper(None, 0, 0, -1, -1)
        
                    
                
            
                
                
        