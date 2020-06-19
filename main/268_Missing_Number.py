class Solution:
    def missingNumber_Gauss(self, nums: List[int]) -> int:
    	# 20:08 - 20:10
        return (len(nums) * (len(nums) + 1)) >> 1 - sum(nums)

    def missingNumber_bit_operation(self, nums: List[int]) -> int:
        # 20:12 - 20:15
        value = len(nums)
        for i, num in enumerate(nums):
            value ^= num ^ i
        return value