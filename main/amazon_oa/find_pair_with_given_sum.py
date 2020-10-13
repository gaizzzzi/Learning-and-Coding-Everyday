def solver(nums, target):
	num_map = {}
	target -= 30
	ans = []
	for i, num in enumerate(nums):
		if target - num in num_map:
			if not ans or max(nums[ans[0]], nums[ans[1]]) < max(num, target- num):
				ans = [num_map[target - num], i]
		num_map[num] = i
	return ans

# [20, 50, 40, 25, 30, 10],90 | [1, 5]
# [1, 10, 25, 35, 60], 90 | [2, 3]
# [50, 20, 10, 40, 25, 30], 90 | [0, 2]
print (solver([30, 50, 40, 25, 30, 30],90))

