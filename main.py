from faker import Faker
import test_data as data

from exams import Examination
from students import Student
from students_group import StudentGroup
from tickets import Tickets

fake = Faker('ru_RU')

exam = Examination('21.07.2024', 'math', 5, data.generate_teacher(),
                   data.generate_duration(), data.generate_student_group())

exam.print_examination_info()
exam.quantity_of_tickets.print_tickets()

print('_________')
exam_tickets = Tickets(5)
exam_tickets.generate_tickets()
exam_tickets.print_tickets()

print('_________')
student_group = StudentGroup(group_number=data.generate_group_number())

students_list = [Student(fake.first_name(), fake.name(), fake.last_name(), i + 1) for i in range(20)]

for student in students_list:
    print(student)
    try:
        student_group.add_student(student)
    except ValueError as e:
        print(e)

print(len(student_group))
