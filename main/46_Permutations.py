class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            if len(nums) == 1:
                return [nums]
            ans = []
            for i in range(len(nums)):
                tmp = helper(nums[:i] + nums[i + 1:])
                for t in tmp:
                    ans.append([nums[i]] + t)
            return ans
        return helper(nums)