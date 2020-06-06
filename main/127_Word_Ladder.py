class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 17:44 - 18:26
        # build map
        word_map = {} # vague search
        wordList += [beginWord]
        
        for i in range(len(wordList)):
            for l in range(len(wordList[0])):
                pre_word = wordList[i][:l] + "*" + wordList[i][l + 1:]
                if not pre_word in word_map:
                    word_map[pre_word] = [wordList[i]]
                else:
                    word_map[pre_word] += [wordList[i]]

        # BFS with memorization
        visited = {beginWord: True}
        bfs = [beginWord]
        count = 1
        
        while bfs:
            tmp = []
            for word in bfs:
                for l in range(len(word)):
                    pre_word = word[:l] + "*" + word[l + 1:]
                    for next_word in word_map[pre_word]:
                        if next_word in visited:
                            continue
                        if next_word == endWord:
                            return count + 1
                        visited[next_word] = True
                        tmp.append(next_word)
            bfs = tmp
            count += 1
        return 0