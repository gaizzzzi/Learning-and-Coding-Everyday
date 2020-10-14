import queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        wordSet = set(wordList)
        visited = {beginWord}
        wordSet.add(beginWord)
        q = queue.Queue()
        q.put((beginWord, 1))
        while not q.empty():
            word, step = q.get()
            for i in range(len(word)):
                for j in range(ord("a"), ord("z") + 1):
                    new_word = word[:i] + chr(j) + word[i + 1:]
                    if new_word == endWord:
                        return step + 1
                    if new_word in wordSet and not new_word in visited:
                        q.put((new_word, step + 1))
                        visited.add(new_word)
        return 0