import collections
def solver(k, keywords, reviews):
    keywords_set = set(keywords)
    word_count = collections.defaultdict(int)
    for review in reviews:
        print(review)
        tmp = ""
        review_set = set()
        for i, char in enumerate(review):
            if char.isalpha():
                tmp += char.lower()
                if i < len(review) - 1:
                    continue
            if tmp:
                if tmp in keywords_set and not tmp in review_set:
                    print(tmp)
                    word_count[tmp] += 1
                    review_set.add(tmp)
                tmp = ""
    print(sorted(word_count.items(), key = lambda x: (-x[1], x[0])))
    return [x for x, y in sorted(word_count.items(), key = lambda x: (-x[1], x[0]))[:k]]

k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
print(solver(k, keywords, reviews))