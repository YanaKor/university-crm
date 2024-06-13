from base_object import Human


class Teacher(Human):

    def __init__(self, first_name, middle_name, surname, subject, degree):
        super().__init__(first_name, middle_name, surname)
        self.subject = subject
        self.degree = degree



