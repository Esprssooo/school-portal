class Portal:
    def __init__(self):
        self.current_user = None
        self.students = {}
        # self.subjects_dict = {}
        # self.subjects_arr = []
        self.faculties = {}
        self.sections = []
        self.scholarships = []

    def add_student(self, student):
        self.students[student.get_username()] = student

    def add_faculty(self, faculty):
        self.faculties[faculty.get_username()] = faculty

    def add_section(self, section):
        self.sections.append(section)

    def add_scholarship(self, scholarship):
        self.scholarships.append(scholarship)

    # def add_subject_arr(self, subject):
    #     self.subjects.append(subject)

    # def add_subject_dict(self, subject):
    #     self.subjects[subject.subject_code] = subject

    def get_current_user(self):
        return current_user

    def login(self, username, password):
        if username in self.students and self.students[username].login(
            username, password
        ):
            self.current_user = self.students[username]
            print(f"Welcome, {self.current_user.full_name}!")
            return self.current_user
        elif username in self.faculties and self.faculties[username].login(
            username, password
        ):
            self.current_user = self.faculties[username]
            print(f"Welcome, {self.current_user.full_name}!")
            return self.current_user
        print("Invalid credentials.")

    def logout(self):
        self.current_user = None
        print("Succesfully logged out.")
