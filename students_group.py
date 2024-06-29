import random
from typing import List

from students import Student


class StudentGroup:
    MAX_STUDENTS = 10

    def __init__(self, group_number=0):
        self.group_number = group_number
        self.students = []

    def __len__(self):
        return len(self.students)

    def __contains__(self, student):
        return student in self.students

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            raise ValueError(f"Group {self.group_number} is full. Cannot add more students.")
        if not isinstance(student, Student):
            raise TypeError("Only instances of Student class can be added to the group.")
        self.students.append(student)

    @classmethod
    def get_groups(cls, students: List[Student]):
        groups = [cls(i + 1) for i in range(len(students) // cls.MAX_STUDENTS+1)]
        current_group_index = 0
        for student in students:
            try:
                groups[current_group_index].add_student(student)
            except ValueError:
                current_group_index += 1
                groups[current_group_index].add_student(student)
        return groups
