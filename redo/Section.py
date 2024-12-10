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

    def view_student_list(self):
        if self.students:
            student_list = f"{self.section_name} students:"
            for student in self.students:
                student_list += f"\n  [{student.student_id}] {student.last_name}, {student.first_name}"
            return student_list
        else:
            return "No students enrolled."

    # def set_subjects(self, subjects):
    #     self.subjects = subjects
