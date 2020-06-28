class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprofix = 0
        preprice = prices[0]
        for price in prices:
            if preprice < price:
                maxprofix += price - preprice
            preprice = price
        return maxprofix