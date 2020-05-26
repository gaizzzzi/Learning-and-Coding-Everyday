class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 20:14
        visited = [False] * len(M)
        
        def dfs_helper(student):
            for i in range(len(M)):
                if M[student][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs_helper(i)
                
        friend_circle = 0
        
        for i in range(len(M)):
            if not visited[i]:
                visited[i] = True
                dfs_helper(i)
                friend_circle += 1
                
        return friend_circle
            