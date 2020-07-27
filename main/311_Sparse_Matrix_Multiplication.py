class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if not A[i][k]:
                    continue
                for j in range(len(B[0])):
                    ans[i][j] += A[i][k] * B[k][j] if B[k][j] else 0
        
        return ans