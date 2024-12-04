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

    def set_subjects(self, subjects):
        self.subjects = subjects
