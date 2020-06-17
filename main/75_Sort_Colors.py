class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 18:05 - 18:15
        start, end, point = 0 , len(nums) - 1, 0
        while point <= end:
            if nums[point] == 0 and point > start:
                nums[start], nums[point] = nums[point], nums[start]
                start += 1
            elif nums[point] == 2 and point < end:
                nums[end], nums[point] = nums[point], nums[end]
                end -= 1
            else:
                point += 1
                