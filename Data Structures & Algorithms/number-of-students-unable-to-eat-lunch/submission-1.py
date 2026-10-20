class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        visited = set()
        k = len(students)*len(sandwiches)
        while len(students)>0 and k>0:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                students = students[1:] + [students[0]]
            k-=1
        return len(students)