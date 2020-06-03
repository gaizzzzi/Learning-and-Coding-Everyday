class Solution:
    def coinChange_dfs_time_out(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        if not coins:
            return -1
        memo = {}
        coins = sorted(list(set(coins)), reverse = True)
        ans = [0]
        def helper(depth, cur_amount, path):
            memo[cur_amount] = depth
            if cur_amount > amount:
                return
            if cur_amount == amount:
                ans = [depth]
                print(path)
                return 
            for coin in coins:
                if not memo.get(cur_amount + coin) or memo[cur_amount + coin] < depth + 1:
                    helper(depth + 1, cur_amount + coin, path + [coin])
                    
        
        depth = helper(0, 0, [])
        if memo.get(amount):
            return memo[amount]
        else:
            -1

    def coinChange_dp_beat_55(self, coins: List[int], amount: int) -> int:
        # dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(min(coins), len(dp)):
            for coin in coins:
                if i - coin > -1:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1

    def coinChange_bfs_fastest_beat_92(self, coins: List[int], amount: int) -> int:
        # bfs
        if not amount:
            return 0
        #coins.sort(reverse = True) # sort doesn't matter
        memo = {}
        bfs = [0]
        count = 0
        while bfs:
            tmp = []
            count += 1
            for b in bfs:
                for coin in coins:
                    if b + coin == amount:
                        return count
                    if b + coin < amount and memo.get(b + coin) is None:
                        tmp.append(b + coin)  
                        memo[b + coin] = True
            bfs = tmp
        return -1