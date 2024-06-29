import random
from faker import Faker

from students import Student


class StudentGroup:
    MAX_STUDENTS = 10

    def __init__(self, group_number):
        self.fake = Faker()
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
        random.shuffle(self.students)

