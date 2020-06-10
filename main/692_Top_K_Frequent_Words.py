class comparison:
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return self.word > other.word
        
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 20:10 - 20:40 
        # heap with size k
        # learned about diy __lt__ functions
        hp = []
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        for word, count in word_map.items():
            if len(hp) == k:
                heappushpop(hp, (count, comparison(word)))
            else:
                heappush(hp, (count, comparison(word)))
        ans = [heappop(hp)[1].word for _ in range(k)]
        return ans[::-1]