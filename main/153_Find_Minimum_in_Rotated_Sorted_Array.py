class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end, pivot = 0, len(nums) - 1, nums[-1]
        while start < end - 1:
            mid = (start + end) // 2
            if nums[mid] < pivot:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]