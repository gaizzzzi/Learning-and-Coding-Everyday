class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # 20:12 - 20:18
       
        s1or2 = abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)

        if (A < C < E < G or E < G < A < C) or (B < D < F < H or  F < H < B < D):
            return s1or2
        
        x, y = sorted([A, C, E, G]), sorted([B, D, F, H])
        s1and2 = abs(x[1] - x[2]) * abs(y[1] - y[2])
        return s1or2 - s1and2