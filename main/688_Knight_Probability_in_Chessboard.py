class Solution:
    def knightProbability_naive_time_out(self, N: int, K: int, r: int, c: int) -> float:
        neighbors = {(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)}
        def helper(_r, _c, step, K):
            if step == K:
                return 1
            prob = 0
            for dr, dc in neighbors:
                r, c = _r + dr, _c + dc
                if -1 < r < N and -1 < c < N:
                    prob += 1/8 * helper(r, c, step + 1, K)
            return prob
        return helper(r, c, 0, K)

# prune
class Solution:
    def knightProbability_beat_99(self, N: int, K: int, r: int, c: int) -> float:
        neighbors = {(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)}
        seen = {}
        def helper(_r, _c, step, K):
            if step == K:
                return 1
            prob = 0
            for dr, dc in neighbors:
                r, c = _r + dr, _c + dc
                if -1 < r < N and -1 < c < N:
                    key = tuple(sorted([abs((N - 1)/2 - r), abs((N - 1)/2 - c)]) + [K - step - 1])
                    if not key in seen:
                        seen[key] = helper(r, c, step + 1, K)
                    prob += 1/8 * seen[key]
            return prob
        return helper(r, c, 0, K)