import random
from faker import Faker

from student import Student


class StudentGroup:
    MAX_STUDENTS = 10

    def __init__(self):
        self.fake = Faker()
        self.group_number = self.generate_group_number()
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

    def generate_group_number(self):
        prefix = self.fake.lexify(text='???')
        number = self.fake.random_int(min=1, max=99)
        return f"{prefix}-{number}"


if __name__ == '__main__':
    student_group = StudentGroup()
    fake = Faker()

    students_list = [Student(fake.first_name(), fake.middle_name(), fake.last_name(), i + 1) for i in range(20)]

    for student in students_list:
        try:
            student_group.add_student(student)
        except ValueError as e:
            print(e)

    print(len(student_group))