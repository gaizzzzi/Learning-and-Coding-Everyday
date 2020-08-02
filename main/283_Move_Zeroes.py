class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = max(i, j)
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
            