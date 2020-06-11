class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 17:58 - 18:10
        # one pass
        p_dict = {}
        for letter in p:
            p_dict[letter] = p_dict.get(letter, 0) + 1
            
        tmp_dict = {}
        start = 0
        ans = []
        for end in range(start, len(s)):
            if s[end] in p_dict:
                tmp_dict[s[end]] = tmp_dict.get(s[end], 0) + 1
            else:
                start = end + 1
                tmp_dict = {}
            if end - start > len(p) - 1:
                tmp_dict[s[start]] -= 1
                start += 1
    
            if end - start == len(p) - 1:
                is_equal = True
                for letter, count in p_dict.items():
                    if not tmp_dict.get(letter) or tmp_dict.get(letter) != count:
                        is_equal = False
                        break
                if is_equal:
                    ans.append(start)
        return ans
                
                
                
            