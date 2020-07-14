class Solution:

    def __init__(self, nums: List[int]):
        self.num_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.num_map[num].append(i)

    def pick(self, target: int) -> int:
        random_idx = int(random.random() * len(self.num_map[target]))
        return self.num_map[target][random_idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)