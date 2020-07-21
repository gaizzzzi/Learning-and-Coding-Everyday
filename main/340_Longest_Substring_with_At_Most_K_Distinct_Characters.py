class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_count, maxlen, head = defaultdict(int), 0, 0
        for tail in range(len(s)):
            char_count[s[tail]] += 1
            if len(char_count) > k:
                head_char = s[head]
                while head < len(s) and s[head] == head_char:
                    char_count[s[head]] -= 1
                    if not char_count[s[head]]:
                        char_count.pop(s[head])
                    head += 1
            if len(char_count) <= k:
                maxlen = max(maxlen, tail - head + 1)
            if head == len(s):
                break
        return maxlen
                