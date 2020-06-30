# 16:57 - 17:18
class Trie:
    def __init__(self):
        self.word_map = {}
    def update(self, word):
        tmp = self.word_map
        for char in word:
            if not char in tmp:
                tmp[char] = {}
            tmp = tmp[char]
        tmp["#"] = None
    def get(self):
        return self.word_map
            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.update(word)
            
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = set()
        
        def helper(_x, _y, word, cur_node):
            if "#" in cur_node:
                ans.update({word})
            for dx, dy in directions:
                x, y = _x + dx, _y + dy
                if -1 < x < len(board) and -1 < y < len(board[0]) and not visited[x][y]:
                    if board[x][y] in cur_node:
                        visited[x][y] = True
                        helper(x, y, word + board[x][y], cur_node[board[x][y]])
                        visited[x][y] = False
                        
        cur_node = trie.get()
        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char in cur_node:
                    visited[x][y] = True
                    helper(x, y, char, cur_node[char])
                    visited[x][y] = False
        
        return list(ans)
                    