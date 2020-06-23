# 15:55 - 16:37
class Solution:
    def findAllConcatenatedWordsInADict_dp_zeiman(self, words: List[str]) -> List[str]:
        word_map = {}
        for word in words:
            if not word:
                continue
            if not len(word) in word_map:
                word_map[len(word)] = {word}
            else:
                word_map[len(word)].add(word)
        
        def helper(word):
            #print(word)
            dp = [1] + [0] * (len(word))
            for i in range(len(word) + 1):
                for lens in lenlist:
                    if lens == len(word) or lens + i > len(word):
                        break
                    if word[i: i + lens]  in word_map[lens]:
                        dp[i + lens] += dp[i]
            #print(dp)
            return dp[-1]
        
        ans = []
        lenlist = sorted(word_map.keys())
        #print(lenlist)
        for word in words:
            if not word:
                continue
            if helper(word):
                ans.append(word)
        
        return ans

    def findAllConcatenatedWordsInADict_dfs_with_memo(self, words: List[str]) -> List[str]:
        def search(word):
            for idx in range(1, len(word)):
                prefix = word[:idx]
                suffix = word[idx:]

                if prefix in wordset and suffix in wordset:
                    wordset.add(word)
                    return True
                if prefix in wordset and search(suffix):
                    wordset.add(suffix)
                    wordset.add(word)
                    return True

            return False

        wordset = set(words)

        return [word for word in words if search(word)]

    def findAllConcatenatedWordsInADict_puredfs_without_memo(self, words):
        d = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True
            
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        
        return res