class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # 20:24 - 21:42
        def merge(ys):
            ys.sort()
            ini_y1, ini_y2 = ys[0]
            interval = 0
            for y1, y2 in ys:
                if y1 <= ini_y2:
                    ini_y2 = max(y2, ini_y2)
                else:
                    interval += ini_y2 - ini_y1
                    ini_y1, ini_y2 = y1, y2
            interval += ini_y2 - ini_y1
            return interval
            
        verticals = []
        for x1, y1, x2, y2 in rectangles:
            verticals.append((x1, y2, y1, 0))
            verticals.append((x2, y2, y1, 1))
        verticals.sort()
        
        ans = 0
        ys = []
        pre_x = None
        for x, y2, y1, is_end in verticals:
            if not pre_x is None and ys:
                ans += (x - pre_x) * merge(ys)
                
            if not is_end:
                ys.append((y1, y2))
                
            else:
                ys.remove((y1, y2))
                
            pre_x = x
                        
        return ans % (1000000007)
