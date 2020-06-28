class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        nums.sort()
        for num in nums:
            if not count[num]:
                continue
            for i in range(k):
                if count[num + i] > 0:
                    count[num + i] -= 1
                else:
                    return False
        return True