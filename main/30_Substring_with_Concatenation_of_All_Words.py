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