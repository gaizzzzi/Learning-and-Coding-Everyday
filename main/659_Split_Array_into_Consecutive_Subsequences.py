class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 17:48 - 19:05
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        end = {}
        for num in nums:
            if not num_count.get(num):
                continue
            num_count[num] -= 1
            if end.get(num - 1):
                end[num - 1] -= 1
                end[num] = end.get(num, 0) + 1
            elif num_count.get(num + 1) and num_count.get(num + 2):
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1
                end[num + 2] = end.get(num + 2, 0) + 1
            else:
                return False
        return True