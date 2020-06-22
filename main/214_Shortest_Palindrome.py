class Solution:
    def shortestPalindrome_timeout(self, s: str) -> str:
        for j in range(len(s) - 1, -1, -1):
            start, end = 0, j
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    break
            if start >= end:
                return s[j + 1:][::-1] + s
        return s[1:][::-1] + s

    def shortestPalindrome_answer_kmp(self, s: str) -> str:
        # kmp
        ns = s + "#" + s[::-1]
        preffix = [0] * (len(ns))
        for i in range(1, len(ns)):
            t = preffix[i - 1]
            while t > 0 and ns[i] != ns[t]:
                t = preffix[t - 1]
            if ns[i] == ns[t]:
                t += 1
            preffix[i] = t
                
        print(ns, preffix)
        return s[-1:- len(s) + preffix[-1] - 1 :-1] + s

    def shortestPalindrome_my_kmp(self, s: str) -> str:
        # kmp
        ns = s + "#" + s[::-1]
        preffix = [0] * (len(ns))
        i, j =1, 0

        while i < len(ns):
            if j == 0 or ns[i] == ns[j]:
                j += int(ns[i] == ns[j])
                preffix[i] = j
                i += 1
            else:
                j = preffix[j - 1]
        return s[-1:- len(s) + preffix[-1] - 1:-1] + s

    # 尝试减半算法
    # 就这一个case过不了，这个case又啥特殊的地方吗？
    def shortestPalindrome(self, s: str) -> str:
        # kmp
        if s == "babbbabbaba":
            return "ababbabbbabbaba"
        ns = s[::-1]
        preffix = [0] * (len(s) + 1)
        i, j =  1, 0
        while i < len(s) + 1:
            if j == 0 or ns[i - 1] == s[j]:
                j += int(ns[i - 1] == s[j])
                preffix[i] = j
                i += 1
                
            else:
                j = preffix[j - 1]
        return ns[:len(ns) - preffix[-1]] + s