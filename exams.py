import random

from faker import Faker
from tickets import Tickets
from teacher import Teacher
from data import teachers_degree
from student_groups import StudentGroup


class Examination:

    def __init__(self, date: str, subject: str, quantity_of_tickets: int):
        self.date = date
        self.fake = Faker('ru_RU')
        self.subject = subject
        self.quantity_of_tickets = Tickets(quantity_of_tickets)
        self.teacher = self.generate_teacher()
        self.duration = self.generate_duration()
        self.student_group = self.generate_student_group()

    def generate_teacher(self):
        first_name = self.fake.first_name()
        middle_name = self.fake.middle_name()
        last_name = self.fake.last_name()
        degree = random.choice(teachers_degree)
        return Teacher(first_name, middle_name, last_name, degree)

    @staticmethod
    def generate_duration():
        return random.randint(60, 180)

    @staticmethod
    def generate_student_group():
        group = StudentGroup()
        return group

    def print_examination_info(self):
        print(f"Предмет: {self.subject}")
        print(f"Преподаватель: {self.teacher}")
        print(f"Продолжительность: {self.duration} минут")
        print("Группа студентов:")
        for student in self.student_group.students:
            print(student)
        print("Билеты:")
        self.quantity_of_tickets.print_tickets()


if __name__ == '__main__':
    exam = Examination('21.07.2024', 'math', 5)

    exam.print_examination_info()
