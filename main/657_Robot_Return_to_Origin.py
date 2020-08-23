class Solution:
    def judgeCircle_beat_7(self, moves: str) -> bool:
        right, up = 0, 0
        for move in moves:
            if move in ["U", "D"]:
                up += (move == "U") - (move == "D")
            if move in ["L", "R"]:
                right += (move == "L") - (move == "R")
        return not (right or up)
    def judgeCircle_beat_93(self, moves: str) -> bool:
        move_counter = collections.Counter(moves)
        return not ((move_counter["U"] - move_counter["D"]) or (move_counter["L"] - move_counter["R"]))