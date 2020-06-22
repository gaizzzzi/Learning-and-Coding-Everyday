class Solution:
    def firstMissingPositive_Onlogn(self, nums: List[int]) -> int:
        missing = 1
        nums.sort()
        for num in nums:
            if num < 1: 
                continue
            if num == missing:
                missing += 1
        return missing

    def firstMissingPositive_On(self, nums: List[int]) -> int:
        if not 1 in nums:
            return 1
        for i in range(len(nums)):
            if nums[i] < 1 or nums[i] > len(nums):
                nums[i] = 1
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        i = 0
        while i < len(nums) and nums[i] < 0:
            i += 1
        
        return i + 1