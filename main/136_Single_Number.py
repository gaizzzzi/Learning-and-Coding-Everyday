class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = 0
        for num in nums:
            value ^= num
        return value