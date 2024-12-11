class Portal:
    def __init__(self):
        self.__current_user = None
        self.__students = {}
        self.__faculties = {}
        self.__sections = []
        self.__scholarships = []

    def add_student(self, student):
        self.__students[student.get_username()] = student

    def add_faculty(self, faculty):
        self.__faculties[faculty.get_username()] = faculty

    def add_section(self, section):
        self.__sections.append(section)

    def add_scholarship(self, scholarship):
        self.__scholarships.append(scholarship)

    def get_scholarships(self):
        return self.__scholarships

    def get_faculty(self, faculty_id):
        return self.__faculties[faculty_id]

    def get_students(self):
        return self.__students

    def get_faculties(self):
        return self.__faculties

    def get_current_user(self):
        return self.__current_user

    def login(self, username, password):
        user = self.__students.get(username) or self.__faculties.get(username)
        if user and user.validate_credentials(username, password):
            user.login()
            return user
        print("Invalid credentials")
        return None
