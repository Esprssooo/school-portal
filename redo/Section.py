class Section:
    def __init__(self, section_name, year, semester):
        self.__section_name = section_name
        self.__year = year
        self.__semester = semester
        self.__students = []
        self.__subjects = []

    def get_section_name(self):
        return self.__section_name

    def get_year(self):
        return self.__year

    def get_semester(self):
        return self.__semester

    def get_students(self):
        return self.__students

    def get_subjects(self):
        return self.__subjects

    def add_student(self, student):
        self.__students.append(student)

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def view_student_list(self):
        if self.__students:
            student_list = f"{self.__section_name} students:"
            for student in self.__students:
                student_list += f"\n  [{student.get_student_id()}] {student.get_last_name()}, {student.get_first_name()}"
            return student_list
        else:
            return "No students enrolled."

    # def set_subjects(self, subjects):
    #     self.subjects = subjects
