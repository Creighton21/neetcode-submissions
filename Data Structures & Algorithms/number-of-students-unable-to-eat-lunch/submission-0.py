class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_students_left = len(students)
        num_students_passed = 0

        while num_students_left != num_students_passed:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                num_students_left -= 1
                num_students_passed = 0
            else:
                num_students_passed += 1
                students.append(students.pop(0))

        
        return num_students_passed