

class NumArray_naive_728ms:
	
    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i : j + 1])

class NumArray_segment_tree_132ms:
    def __init__(self, nums: List[int]):
        n = len(nums)
        while (n & (n - 1)) or n < 2:
            nums.append(0)
            n += 1
        self.seg_tree = [0] * (n - 1) + nums 
        self.n = n
        j = 2 * n - 2
        while j > 0:
            self.seg_tree[(j - 1) // 2] = self.seg_tree[j] + self.seg_tree[j - 1]
            j -= 2

    def update(self, i: int, val: int) -> None:
        i = i + self.n - 1
        diff = val - self.seg_tree[i]
        while i >= 0:
            self.seg_tree[i] += diff
            i = (i - 1) // 2
            
    def sumRange(self, i: int, j: int) -> int:
        i, j = i + self.n - 1, j + self.n - 1
        tmp_sum = 0
        while i <= j:
            if not (i & 1):
                tmp_sum += self.seg_tree[i]
                i += 1
            if (j & 1):
                tmp_sum += self.seg_tree[j]
                j -= 1
            i, j = (i - 1) // 2, (j - 1) // 2
        
        return tmp_sum

# BI Tree
class NumArray_BI_Tree_144ms:
    def __init__(self, nums: List[int]):
        self.orig_array = [0] * len(nums)
        self.BITree = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])
        
    def update(self, i: int, val: int) -> None:
        diff = val - self.orig_array[i] 
        j = i + 1
        while j < len(self.BITree):
            self.BITree[j] += diff
            j += j & (-j)
        self.orig_array[i] += diff
        
    def sumRange(self, i: int, j: int) -> int:
        def find_sum(i):
            i += 1
            tmp_sum = 0
            while i > 0:
                tmp_sum += self.BITree[i]
                i -= i & (-i)
            return tmp_sum
        return find_sum(j) - find_sum(i - 1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)