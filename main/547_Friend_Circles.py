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

    def findCircleNum_Union_find(self, M: List[List[int]]) -> int:
        parent = [i for i in range(len(M))]
        rank = [0] * len(M)

        def find_parent(x):
            if x != parent[x]:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x, y):
            parent_x, parent_y = find_parent(x), find_parent(y)

            if parent_x == parent_y:
                return

            if rank[parent_x] > rank[parent_y]:
                parent[parent_y] = parent_x
            elif rank[parent_x] < rank[parent_y]:
                parent[parent_x] = parent_y
            else:
                parent[parent_y] = parent_x
                rank[parent_y] += 1

        for i in range(len(M)):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)

        circle = set()
        for i in range(len(M)):
            circle.add(find_parent(i))
        
      
        return len(circle)




        
            