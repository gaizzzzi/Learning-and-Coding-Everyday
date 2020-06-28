class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        dic = {}
        maxcount = 1
        
        def prime(_y, _x):
            y, x = _y, _x
            while y % x:
                tmp = x
                x = y % x
                y = tmp
            return _y // x, _x // x  
            
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1:]):
                dx, dy = x2 - x1, y2 - y1
                
                # calculate slope k and intercept b
                if dx == 0:
                    k, b = 'inf', x1
                else:
                    k = (k1, k2) = prime(dy, dx)
                    b = (b1, b2) = prime(y1 * k2 - x1 * k1, k2)
                
                # update dic
                if not (k, b) in dic:
                    dic[(k, b)] = {(x1, y1, i), (x2, y2, j + i + 1)}
                else:
                    dic[(k, b)].update({(x1, y1, i), (x2, y2, j + i + 1)})
                
                # update maxcount
                if len(dic[(k, b)]) > maxcount:
                    maxcount = len(dic[(k, b)])
                    
        return maxcount