class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if not k:
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1] == 0:
                    return True
            return False
        
        mod_set, pre_sum = {0: -1}, 0
        for i, num in enumerate(nums):
            pre_sum += num
            tmp = pre_sum % k
            if not tmp in mod_set:
                mod_set[tmp] = i
            elif i - mod_set[tmp] > 1:
                return True
        return False