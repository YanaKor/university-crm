import random

from student import Student

# class StudentGroup:
#
#     def __init__(self,  group_number, schedule):
#         self.group_number = group_number
#         self.schedule = schedule
#         self.students = []
#
#     def __len__(self):
#         return len(self.students)
#
#     def __contains__(self, student):
#         return student in self.students
#
#     def add_student(self, student):
#         if len(self.students) >= 10:
#             raise ValueError("Group is full. Cannot add more students.")
#         self.students.append(student)
#         random.shuffle(self.students)


class StudentGroup:
    def __init__(self, group_number, schedule):
        self.group_number = group_number
        self.schedule = schedule
        self.students = []

    def __len__(self):
        return len(self.students)

    def __contains__(self, student):
        return student in self.students

    def add_student(self, student):
        if len(self.students) >= 10:
            raise ValueError(f"Group {self.group_number} is full. Cannot add more students.")
        self.students.append(student)
        random.shuffle(self.students)


class StudentGroupCollection:
    def __init__(self, num_groups, schedule):
        self.groups = [StudentGroup(i + 1, schedule) for i in range(num_groups)]

    def __len__(self):
        return sum(len(group) for group in self.groups)

    def __contains__(self, student):
        for group in self.groups:
            if student in group:
                return True
        return False

    def add_student(self, student):
        for group in self.groups:
            try:
                group.add_student(student)
                return
            except ValueError:
                pass
        raise ValueError("All groups are full. Cannot add more students.")


# Example usage
student_group_collection = StudentGroupCollection(5, "Schedule 1")

students = [Student("Student1", "Lastname1", 20, 1),
            Student("Student2", "Lastname2", 20, 1),
            Student("Student3", "Lastname3", 20, 1),
            Student("Student4", "Lastname4", 20, 2),
            Student("Student5", "Lastname5", 20, 2),
            Student("Student6", "Lastname6", 20, 3),
            Student("Student7", "Lastname7", 20, 3),
            Student("Student8", "Lastname8", 20, 4),
            Student("Student9", "Lastname9", 20, 4),
            Student("Student10", "Lastname10", 20, 5),
            Student("Student11", "Lastname11", 20, 5),
            Student("Student12", "Lastname12", 20, 5)]

for student in students:
    try:
        student_group_collection.add_student(student)
    except ValueError as e:
        print(e)

print(len(student_group_collection))
