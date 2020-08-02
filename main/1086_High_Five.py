class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students_t5 = defaultdict(list)
        for student_id, score in items:
            if len(students_t5[student_id]) == 5:
                heappushpop(students_t5[student_id], score)
            else:
                heappush(students_t5[student_id], score)
        return [[x, int(sum(y) / 5)] for x, y in students_t5.items()]