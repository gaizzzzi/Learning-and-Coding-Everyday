class Leaderboard:

    def __init__(self):
        self.score_map = {} # key = playId, value = scoreidx in self.score_list
        
    def addScore(self, playerId: int, score: int) -> None:
        self.score_map[playerId] = self.score_map.get(playerId, 0) + score
        
    def top(self, K: int) -> int:
        # partition
        score_list = list(self.score_map.values()) #[[playId, score]]
        def helper(lo, hi, score_list):
            left, right = lo, hi
            random_index = int(random.random() * (hi - lo) + lo)
            score_list[lo], score_list[random_index] = score_list[random_index], score_list[lo]
            pivot = score_list[lo]
            while left < right:
                while (left < hi) and (score_list[left] >= pivot):
                    left += 1
                while (right > lo) and (score_list[right] <= pivot):
                    right -= 1
                if (left < right):
                    score_list[left], score_list[right] = score_list[right], score_list[left]
            score_list[lo], score_list[right] = score_list[right], score_list[lo]
            
            if right == K - 1:
                return sum(score_list[:K])
            elif right < K - 1:
                return helper(right + 1, hi, score_list)
            else:
                return helper(lo, right - 1, score_list)
            
        return helper(0, len(score_list) - 1, score_list)
        
    def reset(self, playerId: int) -> None:
        self.score_map[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)