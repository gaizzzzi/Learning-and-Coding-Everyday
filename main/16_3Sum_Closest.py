class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = [float('inf'), 0]
        for i in range(len(nums)):
            new_t = target - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if abs(nums[j] + nums[k] - new_t) < ans[0]:
                    ans = [abs(nums[j] + nums[k] - new_t), nums[i] + nums[j] + nums[k]]
                if nums[j] + nums[k] == new_t:
                    return target
                elif nums[j] + nums[k] > new_t:
                    k -= 1
                else:
                    j += 1
        return ans[1]