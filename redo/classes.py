class User:
    def __init__(self, first_name, last_name, role, user_id):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.role = role
        self.__username = user_id
        self.__password = "1234"
        self.is_password_default = True


class Student(User):
    def __init__(self, first_name, last_name, student_count, section):
        user_id = f"S{student_count}"
        super().__init__(first_name, last_name, "student", user_id)
        self.student_id = user_id
        self.section = section
        self.year = section.year
        self.semester = section.semester
        self.subjects = []


class Faculty(User):
    def __init__(self, first_name, last_name, faculty_count):
        user_id = f"F{faculty_count}"
        super().__init__(first_name, last_name, "faculty", user_id)
        self.faculty_id = user_id


class Subject:
    def __init__(self, subject_code, subject_name, units):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.units = units


class Section:
    def __init__(self, section_name, year, semester):
        self.section_name = section_name
        self.year = year
        self.semester = semester
        self.students = []
        self.subjects = []

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)


class SchoolPortal:
    def __init__(self):
        self.users = []
        self.sections = []

    def add_user(self, user):
        self.users.append(user)

    def add_section(self, section):
        self.sections.append(section)
