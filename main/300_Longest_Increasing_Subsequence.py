class Solution:
    def lengthOfLIS_dp(self, nums: List[int]) -> int:
        # 21:49 - 21:55
        # dp 
        if not nums:
            return 0
        maxlen = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxlen = max(maxlen, dp[i])
        return maxlen

    def lengthOfLIS_increasing_stack_binary_search_beat_96(self, nums: List[int]) -> int:
        def bisearch(nums, target):
            start, end = 0, len(nums) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid
                else:
                    end = mid
            if nums[start] >= target:
                return start
            return end
        
        stack = []
        for x in nums:
            if not stack or stack[-1] < x:
                stack.append(x)
            else:
                pos = bisearch(stack, x)
                stack[pos] = x
        return len(stack)