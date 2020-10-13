def lengthOfLongestSubstring(self, s: str) -> int:
    left, right = 0, 0
    longest_len = 0
    counter = defaultdict(int)
    while right < len(s):
        while counter[s[right]] > 0:
            counter[s[left]] -= 1
            left += 1
        longest_len = max(longest_len, right - left + 1)
        counter[s[right]] += 1
        right += 1
        
def lengthOfLongestSubstring(self, s: str) -> int:
    left, right = 0, 0
    longest_len = 0
    counter = defaultdict(int)
    while right < len(s):
        if s[right] in counter and counter[s[right]] >= left:
            left = counter[s[right]] + 1
        counter[s[right]] = right
        right += 1
        longest_len = max(longest_len, right - left)
    return longest_len

