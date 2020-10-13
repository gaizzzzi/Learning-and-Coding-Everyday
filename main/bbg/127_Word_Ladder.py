import queue
def ladderLength(begin, end, wordList):
    word_set = set(wordList + [begin])
    if not end in word_set:
        return 0
    q = queue.Queue()
    q.put((begin, 1))
    while not q.empty():
        word, step = q.get()
        tmp_set = set()
        for i in range(len(word)):
            for order in range(ord("a"), ord("z") + 1):
                new_word = word[:i] + chr(order) + word[i + 1:]
                if new_word == end:
                    return step + 1
                if new_word in word_set:
                    q.put((new_word, step + 1))
                    tmp_set.add(new_word)
        word_set -= tmp_set
    return 0
