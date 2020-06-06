class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 18:37 - 18:58
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if nums[-1] < nums[mid]:
                if nums[-1] < target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[-1]:
                    start = mid
                else:
                    end = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        
        return -1