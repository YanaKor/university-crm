import random

from faker import Faker

from teacher import Teacher
from data import teachers_degree
from students_group import StudentGroup

fake = Faker('ru_RU')


class GenerateTestData:

    @staticmethod
    def generate_teacher():
        first_name = fake.first_name()
        middle_name = fake.middle_name()
        last_name = fake.last_name()
        degree = random.choice(teachers_degree)
        return Teacher(first_name, middle_name, last_name, degree)

    @staticmethod
    def generate_exam_duration():
        return random.randint(60, 180)

    @staticmethod
    def generate_student_group():
        group = StudentGroup()
        return group
