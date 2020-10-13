# 1. dfs, visited, no-duplicate

def permutaion(nums): # returns [[]]
    ans = set()
    def helper(nums, record):
        if len(record) == 0:
            ans.append(tuple(record))
            return
        for i, num in enumerate(nums):
            helper(nums[:i] + nums[i + 1:], record + [num])

    helper(nums, [])
    return [list(permuts) for permuts in ans]

def permutaion(nums): # returns [[]]
    ans = []
    nums.sort()
    def helper(nums, record):
        if len(nums) == 0:
            ans.append(record)
            return
        last_value = float('inf')
        for i, num in enumerate(nums):
            if last_value != num:
                helper(nums[:i] + nums[i + 1:], record + [num])
                last_value = num

    helper(nums, [])

    return ans

    # [0,1,2,3,4]
    # [2, 1, 0, 3, 4]
    # 1st of dfs, idx = 2
    # 2nd: idx 0 -> 5 (idx == 2) 3
    # 3rd: rule out(2, 3)
