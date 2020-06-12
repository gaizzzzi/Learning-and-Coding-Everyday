class Solution:
    def largestOverlap_timeout(self, A: List[List[int]], B: List[List[int]]) -> int:
        # 22:04 - 23:04
        visited_map = {}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def helper(x1, y1, x2, y2):
            if not visited_map.get((x1, y1, x2, y2)):
                visited_map[(x1, y1, x2, y2)] = True
            else:
                return
            self.count += 1
            for dx, dy in directions:
                newx1 = x1 + dx
                newy1 = y1 + dy
                newx2 = x2 + dx
                newy2 = y2 + dy
                if -1 < newx1 < len(A) and -1 < newy1 < len(A) and \
                    -1 < newx2 < len(A) and -1 < newy2 < len(A) and \
                    not visited[newx1][newy1] and A[newx1][newy1] == B[newx2][newy2] == 1:
                    visited[newx1][newy1] = True
                    #print("new",newx1, newy1, newx2, newy2)
                    helper(newx1, newy1, newx2, newy2)
        
        A_1, B_1 = [], []
        
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]:
                    A_1.append((i, j))
                if B[i][j]:
                    B_1.append((i, j))
                    
        self.ans = 0
        if len(B_1) > len(A_1):
            A_1, B_1 = B_1, A_1
            A, B = B, A
        if not A_1 or not B_1:
            return 0
        for i in range(len(A_1)):
            tmp = A_1[i:] + A_1[:i]
            for j in range(len(B_1)):
                dx, dy = B_1[j][0] - tmp[0][0], B_1[j][1] - tmp[0][1]
                visited = [[False] * len(A) for _ in range(len(A))]
                self.count = 0
                for x1, y1 in tmp:
                    x2, y2 = x1 + dx, y1 + dy
                    if -1 < x2 < len(A) and -1 < y2 < len(A) and \
                        not visited[x1][y1] and B[x2][y2]:
                        visited[x1][y1] = True
                        helper(x1, y1, x2, y2)
                self.ans = max(self.ans, self.count)
        return self. ans


    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # 23:04 - 23:34
        A_1, B_1 = [], [] 
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]:
                    A_1.append((i, j))
                if B[i][j]:
                    B_1.append((i, j))
                    
        ans = 0
        dis = {}
        for x1, y1 in A_1:
            for x2, y2 in B_1:
                tmp = (x1 - x2, y1 - y2)
                dis[tmp] = dis.get(tmp, 0) + 1
                ans = max(ans, dis[tmp])
        return ans