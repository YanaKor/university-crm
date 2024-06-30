import random

from faker import Faker

from persons.teacher import Teacher
from data import teachers_degree
from students_group import StudentGroup

fake = Faker()


class TestDataGenerator:

    @staticmethod
    def generate_teacher():
        first_name = fake.first_name()
        last_name = fake.last_name()
        degree = random.choice(teachers_degree)
        return Teacher(first_name, last_name, degree)

    @staticmethod
    def generate_exam_duration():
        return random.randint(60, 180)

    @staticmethod
    def generate_student_group():
        group = StudentGroup()
        return group
