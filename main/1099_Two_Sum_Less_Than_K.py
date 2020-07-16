class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i, j = 0, len(A) - 1
        maxval = float('-inf')
        while i < j:
            if A[i] + A[j] >= K:
                j -= 1
            else:
                maxval = max(maxval, A[i] + A[j])
                i += 1
        return maxval if maxval > float('-inf') else -1