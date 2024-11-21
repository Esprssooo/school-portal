from abc import ABC, abstractmethod


# Abstraction: Base class for User
class User(ABC):
    def __init__(self, username: str, name: str, email: str, password: str):
        self._username = username
        self._name = name
        self._email = email
        self._password = password  # Encapsulation: Store password securely

    @abstractmethod
    def display_info(self):
        pass

    def get_username(self):
        return self._username

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def check_password(self, password: str) -> bool:
        return self._password == password


# Student class with login functionality
class Student(User):
    def __init__(
        self, username: str, name: str, email: str, password: str, section: str
    ):
        super().__init__(username, name, email, password)
        self._section = section
        self._grades = {}

    def display_info(self):
        return f"Student: {self.get_name()} ({self.get_username()}) | Section: {self._section}"

    def add_grade(self, subject: str, grade: float):
        self._grades[subject] = grade

    def view_grades(self):
        return {subject: grade for subject, grade in self._grades.items()}

    def get_section(self):
        return self._section


# Faculty class
class Faculty(User):
    def __init__(self, username: str, name: str, email: str, password: str):
        super().__init__(username, name, email, password)
        self._sections = {}

    def display_info(self):
        return f"Faculty: {self.get_name()} ({self.get_username()})"

    def assign_grade(self, student: Student, subject: str, grade: float):
        if student.get_section() in self._sections:
            student.add_grade(subject, grade)
        else:
            print(f"{student.get_name()} is not in your section.")

    def add_section(self, section_name: str):
        self._sections[section_name] = []

    def view_section_students(self, section_name: str):
        if section_name in self._sections:
            return self._sections[section_name]
        else:
            print(f"No students in section {section_name}.")
            return []


# Section class
class Section:
    def __init__(self, section_name: str):
        self._section_name = section_name
        self._students = []

    def add_student(self, student: Student):
        self._students.append(student)

    def get_students(self):
        return [student.get_name() for student in self._students]

    def get_section_name(self):
        return self._section_name


# Grade class
class Grade:
    def __init__(self, student: Student, subject: str, grade: float):
        self._student = student
        self._subject = subject
        self._grade = grade

    def get_grade_info(self):
        return f"{self._student.get_name()} - {self._subject}: {self._grade}"


# SchoolPortal class with login functionality
class SchoolPortal:
    def __init__(self):
        self._users = {}  # A dictionary of all users (both students and faculty)
        self._sections = {}  # A dictionary of all sections
        self._grades = []  # All grades
        self._logged_in_user = None  # Track logged in user

    def add_user(self, user: User):
        self._users[user.get_username()] = user

    def get_user(self, username: str):
        return self._users.get(username)

    def add_section(self, section: Section):
        self._sections[section.get_section_name()] = section

    def assign_student_to_section(self, student: Student, section_name: str):
        section = self._sections.get(section_name)
        if section:
            section.add_student(student)
        else:
            print(f"Section {section_name} does not exist.")

    def record_grade(self, student: Student, subject: str, grade: float):
        grade_record = Grade(student, subject, grade)
        self._grades.append(grade_record)

    def view_student_grades(self, student: Student):
        grades = [
            grade.get_grade_info()
            for grade in self._grades
            if grade._student == student
        ]
        return grades

    def login(self, username: str, password: str):
        user = self._users.get(username)
        if user and user.check_password(password):
            self._logged_in_user = user
            print(f"Login successful: Welcome {user.get_name()}!")
            return True
        else:
            print("Login failed: Invalid username or password.")
            return False

    def logout(self):
        if self._logged_in_user:
            print(f"Goodbye {self._logged_in_user.get_name()}.")
            self._logged_in_user = None
        else:
            print("No user currently logged in.")

    def current_user(self):
        return self._logged_in_user


# Example usage:
portal = SchoolPortal()

# Create students with passwords
student1 = Student("s001", "Alice", "alice@example.com", "password123", "A1")
student2 = Student("s002", "Bob", "bob@example.com", "password456", "A1")

# Create faculty with passwords
faculty1 = Faculty("f001", "Prof. John", "john@school.com", "faculty123")

# Create sections
section_a1 = Section("A1")
section_b1 = Section("B1")

# Add users and sections to the portal
portal.add_user(student1)
portal.add_user(student2)
portal.add_user(faculty1)
portal.add_section(section_a1)
portal.add_section(section_b1)

# Assign students to sections
portal.assign_student_to_section(student1, "A1")
portal.assign_student_to_section(student2, "A1")

# Faculty assigns grades
faculty1.assign_grade(student1, "Math", 95.0)
faculty1.assign_grade(student2, "Math", 89.0)

# Student logs in and views grades
portal.login("s001", "password123")  # Alice logs in
if portal.current_user():
    student = portal.current_user()
    print(student.view_grades())

# Faculty views section students
print(faculty1.view_section_students("A1"))

# Logout
portal.logout()
