def solver(s, k):
    char_idx = {}
    start = 0
    res = set()
    for end, char in enumerate(s):
        if char in char_idx and char_idx[char] + k > end:
            start = char_idx[char] + 1
        if end - start + 1 >= k:
            res.add(s[start:end + 1])
            start += 1
        char_idx[char] = end

    return list(res)
#s, k = "awaglknagawunagwkwagl", 4
s, k = "abacab", 3
s, k = "abcabc", 3
print(solver(s, k))
