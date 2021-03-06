class Solution:

    def alienOrder_bfs(self, words: List[str]) -> str:
        # 00:12 - 01:45
        
        # initialize topological indegree list
        indegree = {}
        for i in range(len(words)):
            for letter in words[i]:
                indegree[letter] = 0
                
        # initialize map and update topological indegree list
        letter_map = {}
        for i in range(1, len(words)):
            for j in range(len(words[i - 1])):
                if j == len(words[i]):
                    return ""
                if words[i - 1][j] != words[i][j]:
                    if not letter_map.get(words[i - 1][j]):
                        letter_map[words[i - 1][j]] = [words[i][j]]
                    else:
                        letter_map[words[i - 1][j]] += [words[i][j]]
                    indegree[words[i][j]] += 1
                    break
        
        # topological sort
        ans = ""
        indegree_zero = [i for i in indegree.keys() if indegree[i] == 0]
        while indegree_zero:
            letter = indegree_zero.pop()
            ans += letter
            if not letter in letter_map:
                continue
            for next_letter in letter_map[letter]:
                indegree[next_letter] -= 1
                if indegree[next_letter] == 0:
                    indegree_zero.append(next_letter)
        
        # check if there exists indegree that never becomes 0 
        if len(ans) != len(indegree.keys()):
            return ""
        
        return ans
            

    def alienOrder_dfs(self, words: List[str]) -> str:
        # initialize topological indegree list
        indegree = {}
        for i in range(len(words)):
            for letter in words[i]:
                indegree[letter] = 0
                
        # initialize map and update topological indegree list
        letter_map = {}
        for i in range(1, len(words)):
            for j in range(len(words[i - 1])):
                if j == len(words[i]):
                    return ""
                if words[i - 1][j] != words[i][j]:
                    if not letter_map.get(words[i - 1][j]):
                        letter_map[words[i - 1][j]] = [words[i][j]]
                    else:
                        letter_map[words[i - 1][j]] += [words[i][j]]
                    indegree[words[i][j]] += 1
                    break

        # dfs
        def topo_dfs(letter):
            dfs_visited[letter] = True
            ans = letter
            if not letter in letter_map:
                return ans
            for next_letter in letter_map[letter]:
                indegree[next_letter] -= 1
                if indegree[next_letter] == 0 and not next_letter in dfs_visited:
                    ans += topo_dfs(next_letter)
            return ans

        # use dfs
        ans = ""
        dfs_visited = {}
        for letter in indegree.keys():
            if indegree[letter] == 0 and not letter in dfs_visited:
                ans += topo_dfs(letter)
        if len(ans) != len(indegree.keys()):
            return ""
        return ans
            
            