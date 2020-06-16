
class Trie:
    def __init__(self, letter = None):
        self.letter = letter
        self.next = {}
        
class StreamChecker:
    # 15:59 - 16:14
    def __init__(self, words: List[str]):
        self.head = Trie()
        for word in words:
            self.node = self.head
            for letter in word:
                if not letter in self.node.next:
                    self.node.next[letter] = Trie(letter)
                self.node = self.node.next[letter]
            self.node.next["#"] = Trie()
        self.cur_node = []

    def query(self, letter: str) -> bool:
        tmp = []
        self.cur_node.append(self.head)
        True_flag = False
        for node in self.cur_node:
            if letter in node.next:
                tmp.append(node.next[letter])
                if "#" in tmp[-1].next:
                    True_flag |= True
                else:
                    True_flag |= False
            else:
                True_flag |= False
        self.cur_node = tmp
        return True_flag

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)