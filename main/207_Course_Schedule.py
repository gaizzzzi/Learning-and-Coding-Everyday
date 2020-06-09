class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 15:14 - 15:20
        # topological sort
        indegree = [0] * numCourses
        course_map = {}
        for course, precourse in prerequisites:
            indegree[course] += 1
            if not precourse in course_map:
                course_map[precourse] = [course]
            else:
                course_map[precourse] += [course]
        indegree_zero = [x for x in range(len(indegree)) if indegree[x] == 0]
        count = 0
        while indegree_zero:
            course = indegree_zero.pop()
            count += 1
            if not course in course_map:
                continue
            for next_course in course_map[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    indegree_zero.append(next_course)
        if count < numCourses:
            return False
        return True
        