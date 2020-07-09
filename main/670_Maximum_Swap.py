class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        count = collections.Counter(s)
        s_map = {}
        for i, digit in enumerate(s):
            s_map[digit] = i
        i = -1
        for digit in sorted(count.keys(), reverse = True):
            n = count[digit]
            while n:
                n, i = n - 1, i + 1
                if digit != s[i]:
                    s[i], s[s_map[digit]] = s[s_map[digit]], s[i]
                    return int("".join(s))
        
        return num