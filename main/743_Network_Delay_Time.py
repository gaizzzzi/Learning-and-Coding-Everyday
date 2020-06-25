# 20:41 - 21:20 dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        time_map = {}
        for u, v, w in times:
            time_map[u] = time_map.get(u, []) + [(v, w)]
        
        
        hp, time = [(0, K)], {}
        
        while hp:
            last_w, u = heappop(hp)
            if u in time:
                continue
            time[u] = last_w
            if not u in time_map:
                continue
            for v, w in time_map[u]:
                if not v in time:
                    heappush(hp, (last_w + w, v))
     
        return -1 if len(time) < N else max(time.values())
        
                
            
        