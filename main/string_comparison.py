def string_comparison(s, t):
	dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
	for i in range(len(s) + 1):
		dp[0][i] = i

	for i in range(len(t) + 1):
		dp[i][0] = i

	for i in range(1, len(t) + 1):
		for j in range(1, len(s) + 1):
			dp[i][j] = min(dp[i - 1][j] + 1,
						dp[i][j - 1] + 1,
						dp[i - 1][j - 1] + int(s[i - 1] != t[i - 1]))

	return dp[i][j] == 1





# dp[i][j] s[:i] == t[:j] the least steps we need to edit
# dp[i][j] =  min(dp[i - 1][j] + 1 # deletion
# 			dp[i][j - 1] + 1 # insertion
# 			dp[i - 1][j - 1] + int(s[i - 1] != t[j - 1]) #replacement)

# # ""a b
# ""0 1 2
# a 1 0 1
# c 2 1 1
# b 3 2 1

# return dp[-1][-1] == 1

