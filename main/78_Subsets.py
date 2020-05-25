class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(pos, subset):
            ans.append(subset)
            for i in range(pos, len(nums)):
                helper(i + 1, subset + [nums[i]])
        helper(0, [])
        return ans