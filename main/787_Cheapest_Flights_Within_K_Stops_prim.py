# 19:50 - 20:03
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = {}
        for u, v, w in flights:
            edges[u] = edges.get(u, []) + [(v, w)]
        hp = [(0, -1, src)] #(weight, stops, src)
        while hp:
            cur_w, cur_stop, u = heappop(hp)
            if cur_stop > K:
                continue
                
            if u == dst:
                return cur_w

            if not u in edges:
                continue
            for v, w in edges[u]:
                heappush(hp, (cur_w + w, cur_stop + 1, v))
            #print(hp)
                
        return -1
                