class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pre_sum, maxsum = [0], 0
        for i in range(len(cardPoints) - k, len(cardPoints) + k):
            pre_sum.append(pre_sum[-1] + cardPoints[i % len(cardPoints)])
            if len(pre_sum) > k:
                maxsum = max(maxsum, pre_sum[-1] - pre_sum[- k - 1])
        return maxsum