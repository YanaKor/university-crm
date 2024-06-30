from persons.human import Human


class Teacher(Human):

    def __init__(self, first_name, last_name, degree):
        super().__init__(first_name, last_name)
        self.degree = degree

    def __str__(self):
        teacher_info = f'{self.first_name} {self.last_name}\n'
        teacher_info += f'Degree: {self.degree}'
        return teacher_info

