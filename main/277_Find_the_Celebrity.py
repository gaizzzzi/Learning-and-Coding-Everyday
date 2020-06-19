class Solution:
    def findCelebrity_timeout(self, n: int) -> int:
        # 13:52 - 13:57
        indegree = [0] * n
        outdegree = [0] * n
        for a in range(n):
            for b in range(n):
                tmp = int(knows(a, b))
                indegree[b] += tmp
                outdegree[a] += tmp
        
        print(indegree, outdegree)
        for i in range(n):
            if indegree[i] == n and outdegree[i] == 1:
                return i
        
        return -1

    def findCelebrity_on(self, n: int) -> int:
        p1, p2 = 0, 0
        for p1 in range(n):
            p2 = 0
            while p2 < n and (p1 == p2 or (p1 != p2 and not knows(p1, p2))) and knows(p2, p1):
                p2 += 1
            if p2 == n:
                return p1
        return -1

    def findCelebrity_on(self, n: int) -> int:
        celebrity_cand = 0
        for person in range(1, n):
            if knows(celebrity_cand, person):
                celebrity_cand = person
        
        for person in range(n):
            if person == celebrity_cand:
                continue
            if not knows(person, celebrity_cand) or knows(celebrity_cand, person):
                return -1
            
        return celebrity_cand