import random

from faker import Faker
from teacher import Teacher
from data import teachers_degree
from students_group import StudentGroup


fake = Faker('ru_RU')


def generate_teacher():
    first_name = fake.first_name()
    middle_name = fake.middle_name()
    last_name = fake.last_name()
    degree = random.choice(teachers_degree)
    return Teacher(first_name, middle_name, last_name, degree)


def generate_duration():
    return random.randint(60, 180)


def generate_student_group():
    group = StudentGroup(generate_group_number)
    return group


def generate_group_number():
    prefix = fake.lexify(text='???')
    number = fake.random_int(min=1, max=99)
    return f"{prefix}-{number}"
