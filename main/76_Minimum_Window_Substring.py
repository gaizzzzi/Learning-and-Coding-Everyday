class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_set = {}
        for char in t:
            char_set[char] = char_set.get(char, 0) + 1
        
        i, j = 0, 0
        count = 0
        char_count = {}
        minlen = len(s) + 1
        mins = ""    
        while j < len(s):
            if s[j] in char_set:
                char_count[s[j]] = char_count.get(s[j], 0) + 1
                if char_count.get(s[j]) <= char_set[s[j]]:
                    count += 1
                
                # moving i if j got adundant letter than set
                while char_count[s[j]] >= char_set[s[j]]:
                    if s[i] in char_set:
                        if char_count.get(s[i]) <= char_set[s[i]]:
                            break
                        if char_count.get(s[i]):
                            char_count[s[i]] -= 1
                    i += 1
                
                # compare min length and add to answer
                if count == len(t):
                    if minlen > j - i + 1:
                        minlen = j - i + 1
                        mins = s[i:j + 1]
            j += 1     
            
        return mins
                    
                
            
            