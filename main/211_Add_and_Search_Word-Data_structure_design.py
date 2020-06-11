class trie:
    def __init__(self, letter):
        self.letter = letter
        self.next = {}
        
class WordDictionary:
    # trie
    # 17:00 - 17:33 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = trie(" ")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.head
        for letter in word:
            if not letter in node.next:
                node.next[letter] = trie(letter)
            node = node.next[letter]
                
        if "#" not in node.next:
            node.next["#"] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(pos, node):
            if pos == len(word):
                return "#" in node.next
            
            if word[pos] == ".":
                q = False
                for letter in node.next:
                    if letter == "#":
                        continue
                    q |= helper(pos + 1, node.next[letter])
                    if q:
                        return True
            elif word[pos] in node.next:
                return helper(pos + 1, node.next[word[pos]])
            return False
            
        return helper(0, self.head)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)