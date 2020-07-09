class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        idx, direction = 0, None
        for i in range(len(A)):
            if i > 0:
                if (direction == 1 and A[i] < A[i - 1]) or (direction == 0 and A[i] > A[i - 1]):
                    return False
                if A[i] != A[i - 1]:
                    direction = A[i] > A[i - 1]
        return True