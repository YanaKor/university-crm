from base_object import Human


class Student(Human):

    def __init__(self, first_name, middle_name, surname, student_group):
        super().__init__(first_name, middle_name, surname)
        self.student_group = student_group
