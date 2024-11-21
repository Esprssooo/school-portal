# i. Seven (7) classes implemented with well-established interactions or relationships.
# ii. Each class must have an initializer method plus three (3) or more methods which should not be redundant with methods from other classes.
# iii. Implement 4 major concepts of OOP in the final output:
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism
# programs = [
#     {
#         "program_name": "Bachelor of Science in Computer Science",
#         "program_abbrev": "BSCS",
#     },
#     {
#         "program_name": "Bachelor of Science in Information Technology",
#         "specialization": "Mobile Development",
#         "program_abbrev": "BSIT - Mob Dev",
#     },
#     {
#         "program_name": "Bachelor of Science in Information Technology",
#         "specialization": "Network Administration",
#         "program_abbrev": "BSCS - Net Ad",
#     },
#     {
#         "program_name": "Bachelor of Science in Entertainment and Multimedia Computing",
#         "program_abbrev": "BSEMC",
#     },
#     {
#         "program_name": "Associate in Computer Technology",
#         "program_abbrev": "ACT",
#     },
# ]


class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.username = username
        self.password = password

    def register():
        pass

    def login():
        pass

    def logout():
        pass


class Student(User):
    student_id = 1

    def __init__(
        self,
        first_name,
        last_name,
        username,
        password,
        program,
        year_level,
        semester,
    ):
        super().__init__(first_name, last_name, username, password)
        self.student_id = Student.student_id
        self.program = program
        self.section = None
        self.year_level = year_level
        self.semester = semester
        self.grades = {}
        self.balance = 0.00
        self.gwa = 0.00

        Student.student_id += 1

    def view_grades(self):
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

    def view_balance(self):
        print(f"Balance: ₱{self.balance}")

    def compute_gwa(self):
        if self.grades:
            total = 0

            for grade in self.grades.values():
                total += grade

            self.gwa = round(total / len(self.grades), 2)

    def view_gwa(self):
        self.compute_gwa()
        print(f"GWA: {self.gwa}")


stu = Student(
    "a",
    "b",
    "test",
    "yes",
    "Bachelor of Science in Computer Science",
    2,
    1,
)
stu.grades = {"OOP": 98, "IML": 92, "IPS": 97}
stu.view_grades()
stu.view_balance()
stu.compute_gwa()
stu.view_gwa()

a = Student(
    "a",
    "b",
    "test",
    "yes",
    "Bachelor of Science in Information Technology",
    2,
    1,
)

print(stu.student_id, a.student_id)
print(stu.program, a.program)


# classes = {"subject": [sections]}
class Faculty(User):
    faculty_id_counter = 1

    def __init__(self, first_name, last_name, username, password, faculty_id, classes):
        super().__init__(first_name, last_name, username, password)
        self.faculty_id = faculty_id
        self.classes = classes

    def view_classes(self):
        print(f"{self.full_name} is handling the following classes:")
        for cls in self.classes:
            print(f"- {cls}")


# class Class:


class Section:
    def __init__(self, year_level, semester, students, subjects):
        section_name = f"CCIS{year_level - 1 + semester}"
        # if program
        # self.section_name = section_name
        self.students = students
        self.subjects = subjects


# class Profile:
#     def __init__(self):
#         self.


# class Subject:
#     def __init__(self, faculty):
#         self.


# class Scholarship:
#     def __init__(self):
#         self.


# def authentication():
#     print("[1] Register")
#     print("[2] Login")
#     print("[0] Exit")
#     select = input("Choose a menu option [1, 2, 0]: ")
#     print("\n------------------------------------------------\n")
#     if select == "1":
#         register()
#     elif select == "2":
#         pass
#         # login()
#     elif select == "0":
#         exit()
#     else:
#         print("Choose a valid option.")


# def register():
#     print("Register")
#     print("Are you a?")
#     print("[1] Student")
#     print("[2] Faculty")
#     role = input("Select: ")

#     if role == '1':

#     # username = input("Username: ")
#     # password = input("Password: ")
#     # user = User(username, password)
#     print("Welcome ")


# authentication()
