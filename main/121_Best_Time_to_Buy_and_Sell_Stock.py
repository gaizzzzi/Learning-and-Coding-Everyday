class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprofix = 0
        minleftprice = prices[0]
        for price in prices[1:]:
            maxprofix = max(maxprofix, price - minleftprice)
            minleftprice = min(minleftprice, price)
        return maxprofix