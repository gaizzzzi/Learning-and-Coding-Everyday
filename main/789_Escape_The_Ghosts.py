class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # 03:30 - 03:39
        dis = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            tmp_dis = abs(x - target[0]) + abs(y - target[1])
            if tmp_dis <= dis:
                return False
        return True
    