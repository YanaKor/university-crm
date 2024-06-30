from faker import Faker
from test_data import TestDataGenerator as data

from exams import Examination
from persons.students import Student
from students_group import StudentGroup
from tickets import Tickets

fake = Faker()

exam = Examination('21.07.2024', 'Mathematics', Tickets(1, '23', 'hgj', ''), data.generate_teacher(),
                   data.generate_exam_duration(), data.generate_student_group())

print(exam)
print('_________')
student_group = StudentGroup()

students_list = [Student(fake.first_name(), fake.last_name(), i + 1) for i in range(56)]

for student in students_list:
    print(student)
    try:
        student_group.add_student(student)
    except ValueError as e:
        print(e)

print(len(student_group))

print('_________')
groups = StudentGroup.get_groups(students_list)

for group in groups:
    print(f"Group {group.group_number}: {', '.join(str(student) for student in group.students)}")
