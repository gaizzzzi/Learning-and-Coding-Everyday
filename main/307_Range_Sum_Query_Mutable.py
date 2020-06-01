
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
        while (n & (n - 1)) != 0 or n < 2:
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
            if not i % 2:
                tmp_sum += self.seg_tree[i]
                i += 1
            if j % 2:
                tmp_sum += self.seg_tree[j]
                j -= 1
            i, j = (i - 1) // 2, (j - 1) // 2
        
        return tmp_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)