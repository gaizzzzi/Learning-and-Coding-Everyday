class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 16:04 - 16:13
        stones_set = set(stones)
        visited = set() #(stone position, k_units to the stone) 
        def helper(k, stone):
            for i in (-1, 0, 1):
                if k + i < 1:
                    continue
                next_stone = stone + k + i
                if next_stone == stones[-1]:
                    return True
                if next_stone in stones_set and not (k + i, next_stone) in visited:
                    visited.add((k + i, next_stone))
                    if helper(k + i, next_stone):
                        return True
            return False
        
        return helper(0, 0)