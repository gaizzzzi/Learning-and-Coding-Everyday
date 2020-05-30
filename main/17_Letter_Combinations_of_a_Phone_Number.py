class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digits = [eval(x) for x in list(digits)]
        
        letter_list = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ans = []
        def helper(depth, l_comb):
            if depth == len(digits):
                ans.append(l_comb)
                return
            
            for i in range(len(letter_list[digits[depth]])):
                helper(depth + 1, l_comb + letter_list[digits[depth]][i])
        
        helper(0, "")
        return ans