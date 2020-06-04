class Solution:
    def findSubstring_Time_Out(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if not words:
            return []
        if len(s) < len(words[0]) * len(words):
            return []
        
        words.sort()
            
        visited = [False] * len(words)
        
        def find_pos(con_s):
            tmp = []
            for i in range(0, len(s) - len(con_s) + 1):
                if s[i:i + len(con_s)] == con_s:
                    tmp.append(i)
            return tmp
                    
        ans = []
        def helper(depth, con_s, visitied):
            if depth == len(words):
                ans.extend(find_pos(con_s))
                return 
            
            last_i = None
            for i in range(len(words)):
                if not visited[i]:
                    if last_i is not None and words[last_i] == words[i]:
                        continue
                    visited[i] = True
                    helper(depth + 1, con_s + words[i], visited)
                    visited[i] = False
                    last_i = i
        
        helper(0, "", visited)
        return ans

class Solution:
    def findSubstring_hash_two_pointers(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0] or not s:
            return []
        
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
            
        ans = []
        for i in range(min(len(words[0]), len(s) - len(words[0]) * len(words) + 1)):
            start, end = i, i
            curr_freq = {}
            while end < len(s) - len(words[0]) + 1:
                while end < len(s) - len(words[0]) + 1 and not s[end: end + len(words[0])] in word_freq:
                    end += len(words[0])
                    curr_freq = {}
                    start = end
                curr_word = s[end: end + len(words[0])]
                if curr_word in word_freq:
                    curr_freq[curr_word] = curr_freq.get(curr_word, 0) + 1
                    while curr_freq[curr_word] > word_freq[curr_word]:
                        curr_freq[s[start: start + len(words[0])]] -= 1
                        start += len(words[0])
                    if end + len(words[0]) - start == len(words) * len(words[0]):
                        ans.append(start)
                end += len(words[0])
        return ans
        
        
                
        