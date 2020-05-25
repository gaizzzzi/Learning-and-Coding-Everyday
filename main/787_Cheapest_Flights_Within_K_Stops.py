class Solution:
    def findCheapestPrice_dfs_Timeout(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = [False] * n
        prices = [[float('inf')] * (K + 1) for i in range(n)]
        #print(prices)
        prices[src] = [0] * (K + 1)
        self.min_price = float('inf')
        def dfs_helper(depth, current_city, price):
            if depth > K:
                return
            for u, v, w in flights:
                if u == current_city:
                    if v == dst:
                        self.min_price = min(self.min_price, price + w)
                    #print(v, depth)
                    if price + w < prices[v][depth]:
                        prices[v][depth] = price + w
                        visited[v] = True
                        dfs_helper(depth + 1, v, price + w)
                        visited[v] = False

        dfs_helper(0, src, 0)
        if self.min_price == float('inf'):
            return -1
        return self.min_price


    def findCheapestPrice_bfs(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        

    def findCheapestPrice_dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices = [[float('inf')] * n for i in range(n)]
        prices[src] = [0] * n
        visited = [False] * n
        flights_map = {}
        for u, v, w in flights:
            if not flights_map.get(u):
                flights_map[u] = [(v, w)]
            else:
                flights_map[u].append((v, w))
        
        heap = [(0, -1, src)] #(price, k, city)
        
        while heap:
            #print(heap[0])
            price, k, city = heappop(heap)
            if k >= K:
                continue
            visited[city] = True
            if flights_map.get(city):
                for (v, w) in flights_map[city]:
                    if not visited[v] and prices[v][k + 1] > prices[city][k] + w and k < K:
                        prices[v][k + 1] = prices[city][k] + w
                        heappush(heap, (prices[city][k] + w, k + 1, v))
                    #print(prices)
            n -= 1
            min_price = min(prices[dst])
        return min_price if min_price < float('inf') else -1         
 



