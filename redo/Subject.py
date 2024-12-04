class Subject:
    def __init__(self, subject_code, subject_name, units, tuition_per_unit, instructor):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.units = units
        self.tuition_per_unit = tuition_per_unit
        self.instructor = instructor

    def add_subject(self, student):
        student.subjects.append(self)

    def drop_subject(self, student):
        student.subjects.remove(self)

    def view_details(self):
        return f"{[self.subject_code] - {self.subject_name}}\n  Units: {self.units}\n  Instructor: {self.instructor}"
