class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_list = []
        user_sequence = defaultdict(list)
        sequence_3 = defaultdict(int)
        for i in range(len(username)):
            user_list.append([timestamp[i], website[i], username[i]])
        user_list.sort()
        for time, web, user in user_list:
            user_sequence[user].append(web)
        
        max_visited, max_visited_seq = 0, []
        for webs in user_sequence.values():
            if len(webs) < 3:
                continue
            user_set = set()
            for i in range(len(webs) - 2):
                for j in range(i + 1, len(webs) - 1):
                    for k in range(j + 1, len(webs)):
                        seq = tuple([webs[i], webs[j], webs[k]])
                        if seq in user_set:
                            continue
                        user_set.add(seq)
                        sequence_3[seq] += 1
                        if max_visited <= sequence_3[seq]:
                            if max_visited < sequence_3[seq] or not max_visited_seq or seq < tuple(max_visited_seq):
                                #print(max_visited, seq)
                                max_visited_seq = list(seq)
                            max_visited = sequence_3[seq]
        return max_visited_seq