class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        pivot = nums[-1]
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > pivot:
                if nums[mid] > target > pivot:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < pivot:
                if nums[mid] <= target <= pivot:
                    left = mid
                else:
                    right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1