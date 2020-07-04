class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index, ans = {}, 0
        for i, char in enumerate(s):
            k, j = index.get(char, [-1, -1])
            ans += (i - j) * (j - k)
            index[char] = [j, i]
        
        for k, j in index.values():
            ans += (len(s) - j) * (j - k)
        return ans % (10 ** 9 + 7)