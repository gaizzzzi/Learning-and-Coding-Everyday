class Solution:
    def findCheapestPrice_dfs_AC_3336ms(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = [False] * n
        prices = [[float('inf')] * (K + 1) for i in range(n)]
        #print(prices)
        prices[src] = [0] * (K + 1)
        flights_map = {}
        for u, v, w in flights:
            if not flights_map.get(u):
                flights_map[u] = [(v, w)]
            else:
                flights_map[u].append((v, w))
        self.min_price = float('inf')
        def dfs_helper(depth, u, price):
            if depth > K:
                return
            if flights_map.get(u):
                for v, w in flights_map[u]:
                    if v == dst:
                        self.min_price = min(self.min_price, price + w)
                    #print(v, depth)
                    if price + w < min(prices[v][:depth + 1]):
                        prices[v][depth] = price + w
                        visited[v] = True
                        dfs_helper(depth + 1, v, price + w)
                        visited[v] = False

        dfs_helper(0, src, 0)
        if self.min_price == float('inf'):
            return -1
        return self.min_price 


    def findCheapestPrice_bfs_AC_92ms(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices = [[float('inf')] * (K + 2) for i in range(n)]
        prices[src] = [0] * (K + 2)
        visited = [False] * n
        flights_map = {}
        for u, v, w in flights:
            if not flights_map.get(u):
                flights_map[u] = [(v, w)]
            else:
                flights_map[u].append((v, w))
        q = queue.Queue()
        q.put(src)
        k = 0
        while not q.empty() and k < K + 1:
            n = q.qsize()
            while n:
                city = q.get()
                if flights_map.get(city):
                    for v, w in flights_map[city]:
                        if min(prices[v][:k + 2]) > prices[city][k] + w: # shrink 4/5 time 
                        #if prices[v][k + 1] > prices[city][k] + w: 
                            prices[v][k + 1] = prices[city][k] + w
                            q.put(v)
                n -= 1
            k += 1
            
        return min(prices[dst]) if min(prices[dst]) < float('inf') else -1

    def findCheapestPrice_dijkstra_AC_60ms(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # elimated distance list
        visited = [False] * n
        flights_map = {}
        for u, v, w in flights:
            if not flights_map.get(u):
                flights_map[u] = [(v, w)]
            else:
                flights_map[u].append((v, w))
        
        heap = [(0, -1, src)] #(price, k, city)
        
        while heap:
            price, k, city = heappop(heap)
            if k > K:
                continue
            if city == dst:
                return price
            visited[city] = True
            if flights_map.get(city):
                for (v, w) in flights_map[city]:
                    if not visited[v]:
                        heappush(heap, (price + w, k + 1, v))
            
            n -= 1
                    
        return -1  

    def findCheapestPrice_DP_AC_116ms(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:      
        # 15min
        dp = [-1] * n
        dp[src] = 0
        flights_map = {}
        for u, v, w in flights:
            if flights_map.get(u):
                flights_map[u].append((v, w))
            else:
                flights_map[u] = [(v, w)]
        
        for k in range(K + 1):
            new_dp = [-1] * n
            new_dp[src] = 0
            for u in range(len(dp)):
                if dp[u] != -1:
                    
                    if flights_map.get(u):
                        for v, w in flights_map[u]:
                            if new_dp[v] == -1 or new_dp[v] > dp[u] + w:
                                new_dp[v] = dp[u] + w
            dp = new_dp
            
        return dp[dst]   
 



