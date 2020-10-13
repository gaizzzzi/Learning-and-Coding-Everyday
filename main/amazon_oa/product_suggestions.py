# trie dictionary
def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    products_map = {}
    for word in products:
        curr = products_map
        for char in word:
            if not char in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = {}

    def helper(curr, count): # get words 
        ans = []
        if "#" in curr:
            ans.append("")
        for char_idx in range(26):
            char = chr(ord("a") + char_idx)
            if not char in curr:
                continue
            if len(ans) < count:
                ans.extend([char + x for x in helper(curr[char], count - len(ans))])
        return ans

    res = [[] for _ in range(len(searchWord))]
    suggestion_num = 3
    curr = products_map
    for i, char in enumerate(searchWord):
        if char in curr:
            res[i] = [searchWord[:i + 1] + x for x in helper(curr[char], suggestion_num)]
            curr = curr[char]
        else:
            break

    return res

# trie instance
class trie:
    def __init__(self):
        self.char = {}
        self.suggestions = []
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = trie()
        for product in sorted(products):
            curr = root
            for char in product:
                if not char in curr.char:
                    curr.char[char] = trie()
                curr = curr.char[char]
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(product)
        
        res = [[] for _ in range(len(searchWord))]
        suggestion_num = 3
        curr = root
        for i, char in enumerate(searchWord):
            if char in curr.char:
                res[i] = curr.char[char].suggestions
                curr = curr.char[char]
            else:
                break

        return res

# hash
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products_map = defaultdict(list)
        for product in sorted(products):
            for i in range(len(product)):
                key = product[:i + 1]
                if len(products_map[key]) < 3:
                    products_map[key].append(product)

        return [products_map[searchWord[:i + 1]] for i in range(len(searchWord))]

# binary search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        def binary_search(word, i):
            left, right = i, len(products) - 1
            while left < right - 1:
                mid = (left + right) // 2
                if products[mid] >= word:
                    right = mid
                else:
                    left = mid
            if products[left] >= word:
                return left
            else:
                return right

        idx = 0
        res = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            idx = binary_search(prefix, idx)
            for j in range(3):
                if idx + j < len(products) and products[idx + j][:i + 1] == prefix:
                    res[i].append(products[idx + j])
        return res



