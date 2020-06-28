class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        leftmin, rightmax = prices[0], prices[-1]
        leftprofix, rightprofix = [0] * len(prices), [0] * (len(prices) + 1)
        
        for i in range(1, len(prices)):
            leftprofix[i] = max(leftprofix[i - 1], prices[i] - leftmin)
            rightprofix[len(prices) - i - 1] = max(rightprofix[len(prices) - i], rightmax - prices[len(prices) - i - 1])
            leftmin = min(leftmin, prices[i])
            rightmax = max(rightmax, prices[len(prices) - i - 1])
            
        maxprofix = 0
        
        for i in range(len(prices)):
            maxprofix = max(maxprofix, leftprofix[i] + rightprofix[i + 1])
            
        
        return maxprofix