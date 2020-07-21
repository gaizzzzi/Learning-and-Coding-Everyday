class Solution:
    def minSubArrayLen_bisearch(self, s: int, nums: List[int]) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(num + pre_sum[-1])
        
        def bisearch(l, r, nums, target):
            while l < r - 1:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m
                else:
                    r = m
            if nums[r] <= target:
                return r
            if nums[l] <= target:
                return l
            else:
                return float('-inf')
                
        minsize = float('inf')
        
        for i in range(1, len(pre_sum)):
            j = bisearch(0, i, pre_sum, pre_sum[i] - s)
            minsize = min(minsize, i - j)
        return minsize if minsize < float('inf') else 0
        
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        minsize = float('inf')
        i, j, tmp_sum = 0, 0, 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            while (tmp_sum >= s):
                minsize = min(minsize, i + 1 - j)
                j += 1
                tmp_sum -= nums[j]
        return minsize if minsize < float('inf') else 0