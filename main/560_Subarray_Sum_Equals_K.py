class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 17:48 - 18:27
        pre_sum = {0: 1}
        sums, ans = 0, 0
        
        for num in nums:
            sums += num
            if pre_sum.get(sums - k):
                ans += pre_sum[sums - k]
            pre_sum[sums] = pre_sum.get(sums, 0) + 1
        return ans