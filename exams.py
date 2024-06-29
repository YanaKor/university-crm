from faker import Faker

from students_group import StudentGroup
from teacher import Teacher
from tickets import Tickets


class Examination:

    def __init__(self, date: str, subject: str, quantity_of_tickets: int, teacher: Teacher, duration,
                 student_group: StudentGroup):
        self.date = date
        self.fake = Faker('ru_RU')
        self.subject = subject
        self.quantity_of_tickets = Tickets(quantity_of_tickets)
        self.teacher = teacher
        self.duration = duration
        self.student_group = student_group

    def print_examination_info(self):
        print(f"Предмет: {self.subject}")
        print(f'Дата проведения экзамена: {self.date}')
        print(f"Преподаватель: {self.teacher}")
        print(f"Продолжительность: {self.duration} минут")
        print("Группа студентов:")
        for student in self.student_group.students:
            print(student)
        print("Билеты:")
        self.quantity_of_tickets.generate_tickets()
        self.quantity_of_tickets.print_tickets()
