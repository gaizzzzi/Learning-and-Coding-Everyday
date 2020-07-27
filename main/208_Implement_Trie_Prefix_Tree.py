class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_node = self.trie
        for char in word:
            if not char in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node["#"] = None
            
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_node = self.trie
        for char in word:
            if not char in cur_node:
                return False
            cur_node = cur_node[char]
        return "#" in cur_node
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.trie
        for char in prefix:
            if not char in cur_node:
                return False
            cur_node = cur_node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)