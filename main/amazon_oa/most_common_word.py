class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        word_count = defaultdict(int)
        word_buffer, max_count, max_count_word = "", 0, ""
        for i, char in enumerate(paragraph):
            if char.isalpha():
                word_buffer += char.lower()
                if i < len(paragraph) - 1:
                    continue
            if word_buffer and not word_buffer in banned_set:
                word_count[word_buffer] += 1
                if max_count < word_count[word_buffer]:
                    max_count, max_count_word = word_count[word_buffer], word_buffer
            word_buffer = ""
        return max_count_word