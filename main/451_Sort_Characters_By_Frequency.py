class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        return "".join([char * num for char, num in count.most_common()])