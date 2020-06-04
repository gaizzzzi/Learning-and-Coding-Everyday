class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]
        accumulate = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= accumulate
            accumulate *= nums[i]
        return ans