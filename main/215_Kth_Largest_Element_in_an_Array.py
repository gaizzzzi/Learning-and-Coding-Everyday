class Solution:
        # simplest way: sort in o(nlogn) time and fetch the kth one with o(1)
        # can we do better?
        # use k-size heap? with o(nlogk) time
        # can we do better? like o(n) time?

    def findKthLargest_ksize_heap(self, nums: List[int], k: int) -> int:
        # 18:30 - 18:34
        hp = []
        for num in nums:
            if len(hp) == k:
                heappushpop(hp, num)
            else:
                heappush(hp, num)
        return hp[0]

    def findKthLargest_random_partition(self, nums: List[int], k: int) -> int:
        # 18:37 - 18:44
        # random partition
        def helper(l, r):
            lo, hi = l, r
            rd = int(random.random() * (r - l) + l)
            nums[rd], nums[l] = nums[l], nums[rd]
            pivot = nums[l]
            while lo < hi:
                while lo < r and nums[lo] >= pivot:
                    lo += 1
                while hi > l and nums[hi] <= pivot:
                    hi -= 1
                if lo < hi:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
    
            nums[l], nums[hi] = nums[hi], nums[l]
            if hi == k - 1:
                return nums[hi]
            if hi < k - 1:
                return helper(hi + 1, r)
            else:
                return helper(l, hi - 1)
            
        return helper(0, len(nums) - 1)