from faker import Faker

from students_group import StudentGroup
from persons.teacher import Teacher
from tickets import Tickets


class Examination:

    def __init__(self, date: str, subject: str, tickets: Tickets, teacher: Teacher, duration,
                 student_group: StudentGroup):
        self.date = date
        self.fake = Faker('ru_RU')
        self.subject = subject
        self.tickets = tickets
        self.teacher = teacher
        self.duration = duration
        self.student_group = student_group

    def __str__(self):
        examination_info = f"Subject: {self.subject}\n"
        examination_info += f'Examination day: {self.date}\n'
        examination_info += f"Teacher: {self.teacher}\n"
        examination_info += f"Duration: {self.duration} minutes\n"
        examination_info += "Students group:\n"
        for student in self.student_group.students:
            examination_info += str(student) + "\n"
        examination_info += "Tickets: \n"
        examination_info += str(self.tickets) + "\n"
        return examination_info

