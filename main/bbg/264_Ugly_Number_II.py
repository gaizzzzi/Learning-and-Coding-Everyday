class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        idx2, idx3, idx5 = 0, 0, 0
        while len(nums) < n:
            min_num = min(2 * nums[idx2], 3 * nums[idx3], 5 * nums[idx5])
            if min_num == 2 * nums[idx2]:
                idx2 += 1
            if min_num == 3 * nums[idx3]:
                idx3 += 1
            if min_num == 5 * nums[idx5]:
                idx5 += 1
            nums.append(min_num)
        return nums[-1]
        