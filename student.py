from base_object import Human
from faker import Faker


class Student(Human):

    def __init__(self, first_name, middle_name, surname, number):
        super().__init__(first_name, middle_name, surname)
        self.number = number
        self.admitted_students = []

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.surname}"

    def add_students_to_list(self):
        self.admitted_students.append(self)


fake = Faker('ru_RU')
students = [Student(fake.first_name(), fake.middle_name(), fake.last_name(), i+1) for i in range(20)]

for student in students:
    student.admitted_students.append(student)

for student in students:
    print(student)
