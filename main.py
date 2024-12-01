from data import sections_data


class User:
    user_id = 1
    users_db = {}

    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.__username = User.user_id
        self.__password = "1234"
        self.is_password_default = True

        User.users_db[self.__username] = self

        User.user_id += 1

    def validate_password(self, password):
        return self.__password == password

    def login(self):
        print(f"\nWelcome, {self.full_name}!")

        if self.is_password_default:
            while True:
                change_password_input = input(
                    "You still have your default password. Would you like to change it now? [Y/n]: "
                ).lower()

                if change_password_input == "n":
                    break

                else:
                    self.change_password()
                    self.is_password_default = False
                    break

    def logout(self):
        print("Successfully logged out.")

    def change_password(self):
        while True:
            check_password = input("\nCurrent password: ")

            if check_password == self.__password:
                while True:
                    new_password = input("\nNew password: ")

                    if not new_password:
                        print("Enter a valid password!")

                    else:
                        confirm_password = input("Confirm password: ")

                        if confirm_password == new_password:
                            print("Successfully changed password")
                            self.__password = new_password
                            break

                        else:
                            print("Password doesn't match")
                break

            else:
                print("You entered the wrong password.")

    def get_username(self):
        return self.__username

    # def get_password(self):
    #     return self.__password


class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_id = self.get_username()
        self.grades = {}
        self.balance = 0.00
        self.gwa = 0.00
        self.scholarship = None


class Faculty(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.faculty_id = self.get_username()
        self.classes = {}

    def view_classes(self):
        print(self.full_name)
        print("Your classes: ")

        if not self.classes:
            print("No classes assigned.")
        else:
            for subject_name, sections in self.classes.items():
                print(f"  {subject_name}: {sections}")

    def grade_students(self, section, period):
        # if period not in ["Prelim", "Midterm", "Final"]:
        #     return

        print(f"Grading students in {section.section_name}")

        for student in section.students:
            while True:
                grade = float(
                    input(
                        f"Enter grade for {student.last_name}, {student.first_name}: "
                    )
                )

                if grade and 0 <= grade <= 100:
                    student.grades[section.subjects[0].subject_code] = grade
                    break
                else:
                    print("Invalid grade. Please enter a value between 0 and 100.")


class Section:
    def __init__(self, section_name, students, subjects):
        self.section_name = section_name
        self.students = students
        self.subjects = subjects

    def add_student(self, student):
        self.students.append(student)


class Subject:
    def __init__(self, subject_name, subject_code, units, instructor):
        self.subject_name = subject_name
        self.subject_code = subject_code
        self.units = units
        self.instructor = instructor


class Scholarship:
    def __init__(self, required_gwa, discount, type):
        self.required_gwa = required_gwa
        self.discount = discount
        self.type = type


scholarships = [
    Scholarship(1.1, 1, "Academic"),
    Scholarship(1.3, 0.75, "Academic"),
    Scholarship(1.5, 0.5, "Academic"),
]

# storing section objects
sections = []
faculties = {}
for section_data in sections_data:
    section_name = section_data["section"]

    students = []
    for name in section_data["names"]:
        student = Student(name["first_name"], name["last_name"])
        students.append(student)

    subjects = []
    for subject_info in section_data["subjects"]:
        instructor_name = f"{subject_info['instructor']['first_name']} {subject_info['instructor']['last_name']}"

        if instructor_name not in faculties:
            faculty = Faculty(
                subject_info["instructor"]["first_name"],
                subject_info["instructor"]["last_name"],
            )
            faculties[instructor_name] = faculty
        else:
            faculty = faculties[instructor_name]

        subject = Subject(
            subject_info["subject_name"],
            subject_info["subject_code"],
            subject_info["units"],
            faculty,
        )
        subjects.append(subject)

        if subject.subject_name not in faculty.classes:
            faculty.classes[subject.subject_name] = []
        faculty.classes[subject.subject_name].append(section_name)

    section = Section(section_name, students, subjects)
    sections.append(section)


def get_login_credentials():
    while True:
        username = input("\nUsername (ID): ")

        if username.isdigit():
            username = int(username)

            if username not in User.users_db:
                print("User not found.")

            user = User.users_db[username]

            password = input("Password: ")

            if user.validate_password(password):
                user.login()
                return user

            else:
                print("Incorrect password.")

        else:
            print("Invalid username.")


current_user = None

while True:
    if current_user is None:
        print("[1] Login")
        print("[0] Exit")
        select = input("Choose a menu option [1, 0]: ")

        if select == "1":
            current_user = get_login_credentials()

            if current_user:
                while True:
                    print("\n[1] View Grades")
                    print("[0] Logout")
                    menu_option = input("Choose a menu option [1, 0]: ")
                    print()

                    if menu_option == "0":
                        current_user.logout()
                        current_user = None
                        break

                    else:
                        print("Invalid option, please try again.")

        elif select == "0":
            print("Exiting...")
            exit()

        else:
            print("Please enter a valid option.\n")


# # print the classes the faculties have
# for faculty in faculties.values():
#     print(f"\n{faculty.first_name} {faculty.last_name}'s Classes:")
#     for subject_name, sections_arr in faculty.classes.items():
#         print(f"  {subject_name}: {sections_arr}")

# # testing faculty methods
# sections[0].subjects[0].instructor.grade_students(sections[0])

# for section in sections:
#     for subject in section.subjects:
#         subject.instructor.view_classes()
#     for student in section.students:
#         print(f"{student.grades}")


# # printing students and subjects per section
# for section in sections:
#     print(f"\n{section.section_name}")
#     # print("  Students:")
#     # for student in section.students:
#     #     print(f"    {student.last_name}, {student.first_name}")
#     # print()

#     print("  Subjects:")
#     for subject in section.subjects:
#         print(f"    [{subject.subject_code}] - {subject.subject_name}")
#         print(
#             f"    Instructor: {subject.instructor.first_name} {subject.instructor.last_name}\n"
#         )
