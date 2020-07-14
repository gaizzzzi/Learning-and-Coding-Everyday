class Solution:
    def longestMountain(self, A: List[int]) -> int:
        maxlen, i, j, is_peak = 0, 0, 0, False
        for j in range(1, len(A)):
            if A[j] > A[j - 1]:
                if is_peak:
                    maxlen = max(maxlen, j - i)
                    i = j - 1
                    is_peak = False
            elif A[j] == A[j - 1]:
                if is_peak:
                    maxlen = max(maxlen, j - i)
                    is_peak = False
                i = j
            else:
                if i != j - 1:
                    is_peak = True
                if not is_peak:
                    i = j
            #print(i,j,maxlen,is_peak)
        return max(maxlen, j - i + 1) if is_peak else maxlen