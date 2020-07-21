class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r - 1:
            m = (l + r) // 2
            if nums[m] - m - nums[0] >= k:
                r = m
            else:
                l = m
        
        if nums[r] - nums[0] - r >= k:
            return nums[0] + r + k - 1
        else:
            return k + r + nums[0]