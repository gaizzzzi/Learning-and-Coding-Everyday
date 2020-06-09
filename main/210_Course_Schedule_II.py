class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 15:27 - 15:32
        # topological sort
        course_map = {}
        indegree = [0] * numCourses
        for course, precourse in prerequisites:
            indegree[course] += 1
            if not precourse in course_map:
                course_map[precourse] = [course]
            else:
                course_map[precourse] += [course]
        
        indegree_zero = [x for x in range(numCourses) if indegree[x] == 0]
        
        ans = []
        while indegree_zero:
            precourse = indegree_zero.pop()
            ans += [precourse]
            if not precourse in course_map:
                continue

            for course in course_map[precourse]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    indegree_zero.append(course)
        if len(ans) < numCourses:
            return []
        return ans


    