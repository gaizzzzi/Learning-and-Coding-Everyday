class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pre_sum = [0]
        for i in range(len(A)):
            pre_sum.append(pre_sum[-1] + A[i])
        
        maxsum = 0
        for i in range(len(A)):
            if i + L > len(A):
                break
            for j in range(len(A)):
                if j + M > len(A):
                    break
                if i <= j < i + L or j <= i < j + M:
                    continue
                maxsum = max(maxsum, pre_sum[i + L] - pre_sum[i] + pre_sum[j + M] - pre_sum[j])
        return maxsum

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pre_sum = [0]
        for i in range(len(A)):
            pre_sum.append(pre_sum[-1] + A[i])
        
        maxsum, maxL, maxM = pre_sum[L + M], pre_sum[L], pre_sum[M] 
        for i in range(L + M + 1, len(A) + 1):
            maxL = max(maxL, pre_sum[i - M] - pre_sum[i - M - L])
            maxM = max(maxM, pre_sum[i - L] - pre_sum[i - M - L])
            maxsum = max(maxsum, maxL + pre_sum[i] - pre_sum[i - M], maxM + pre_sum[i] - pre_sum[i - L])
            
        return maxsum