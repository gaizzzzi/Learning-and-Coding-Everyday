class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 23:07 - 23:22
        ans = []
        def helper(pos, record):
            if len(record) > 1:
                    ans.append(record)
            if pos == len(nums):
                return
            found = {}
            for i in range(pos, len(nums)):
                if not record or nums[i] >= record[-1]:
                    if nums[i] in found:
                        continue
                    helper(i + 1, record + [nums[i]])
                    found[nums[i]] = True
        helper(0, [])
        return ans