from base_object import Human


class Teacher(Human):

    def __init__(self, first_name, middle_name, last_name, degree):
        super().__init__(first_name, middle_name, last_name)
        self.degree = degree

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

