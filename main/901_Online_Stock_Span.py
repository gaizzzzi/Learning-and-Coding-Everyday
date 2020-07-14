class StockSpanner:

    def __init__(self):
        self.stock, self.span = [], []
        
    def next(self, price: int) -> int:
        tmp = len(self.stock) - 1
        self.stock.append(price)
        self.span.append(1)
        while tmp > -1 and self.stock[tmp] <= price:
            self.span[-1] += self.span[tmp]
            tmp -= self.span[tmp]
        return self.span[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)