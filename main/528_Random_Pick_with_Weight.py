class Solution:

    def __init__(self, w: List[int]):
        total_sum = sum(w)
        self.cum_sum = [w[0]/total_sum]
        for i in range(1, len(w)):
            self.cum_sum.append(self.cum_sum[i - 1] + w[i]/total_sum)

    def pickIndex(self) -> int:
        random_factor = self.cum_sum[-1] * random.random()
        
        # binary search to find which interval the random factor locates
        start = 0
        end = len(self.cum_sum) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.cum_sum[mid] == random_factor:
                return mid
            elif self.cum_sum[mid] < random_factor:
                start = mid
            else:
                end = mid
        if self.cum_sum[start] < random_factor:
            return end
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()