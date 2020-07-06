import queue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord in wordList:
            return []
        vague_map = defaultdict(set)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                vague_map[word[:i] + "*" + word[i + 1:]].add(word)
        
        q = queue.Queue()
        q.put([beginWord])
        visited = {beginWord}
        ans = []
        found = False
        while not q.empty() and not found:
            qsize = q.qsize()
            tmp_visited = set()
            while qsize:
                qsize -= 1
                words = q.get()
                word = words[-1]
                for i in range(len(word)):
                    vague = word[:i] + "*" + word[i + 1:]
                    for next_word in vague_map[vague]:
                        if next_word == endWord:
                            found = True
                            ans.append(words + [next_word])
                            break
                        if not next_word in visited:
                            tmp_visited.add(next_word)
                            q.put(words + [next_word])
            visited.update(tmp_visited)
        return ans
                        
                
        