# i. Seven (7) classes implemented with well-established interactions or relationships.
# ii. Each class must have an initializer method plus three (3) or more methods which should not be redundant with methods from other classes.
# iii. Implement 4 major concepts of OOP in the final output:
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism


class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.username = username
        self.password = password


class Student(User):
    student_id = 1

    def __init__(
        self,
        first_name,
        last_name,
        username,
        password,
        year,
        semester,
    ):
        super().__init__(first_name, last_name, username, password)
        self.student_id = Student.student_id
        self.section = None
        self.year = year
        self.semester = semester
        self.subjects = {}
        self.balance = 0.00
        self.gwa = 0.00

        Student.student_id += 1

    def view_grades(self):
        for subject, grade in self.subjects.items():
            print(f"{subject}: {grade}")

    def view_balance(self):
        print(f"Balance: ₱{self.balance}")

    def compute_gwa(self):
        if self.subjects:
            total = 0

            for grade in self.subjects.values():
                total += grade

            self.gwa = round(total / len(self.subjects), 2)

    def view_gwa(self):
        print(f"GWA: {self.gwa}")


stu = Student(
    "a",
    "b",
    "test",
    "yes",
    2,
    1,
)
stu.subjects = {"OOP": 98, "IML": 92, "IPS": 97}
stu.view_grades()
stu.view_balance()
stu.compute_gwa()
stu.view_gwa()

a = Student(
    "a",
    "b",
    "test",
    "yes",
    2,
    1,
)

print(stu.student_id, a.student_id)


# classes = {"subject": [sections]}
class Faculty(User):
    def __init__(self, faculty_id, classes):
        self.faculty_id = faculty_id
        self.classes = classes


# class Class:


# class Section:
#     def __init__(self, section_name, students):
#         self.section_name = section_name
#         self.students = students

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
