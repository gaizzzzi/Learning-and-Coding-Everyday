def solver(s, startIndices, endIndices):
    
    pre_col = None
    dp = [0] * (len(s) + 1)
    for i in range(1, len(dp)):
        if s[i - 1] == "|":
            if pre_col is not None:
                dp[i] = dp[i - 1] + i - 1 - pre_col
            pre_col = i
        else:
            dp[i] = dp[i - 1]
    print(dp)
    return [dp[endIndices[i]] - dp[startIndices[i]] for i in range(len(startIndices))]

s = '|**|*|*'
startIndices = [1, 1]
endIndices = [5, 6]
s = '*|*|'
startIndices = [1]
endIndices = [3]
s = '*|*|*|'
startIndices = [1,2,2]
endIndices = [3,6,5]

print(solver(s, startIndices, endIndices))
