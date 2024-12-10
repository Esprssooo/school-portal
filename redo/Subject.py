class Subject:
    def __init__(self, subject_code, subject_name, units, tuition_per_unit, instructor):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.units = units
        self.tuition_per_unit = tuition_per_unit
        self.instructor = instructor

    def view_details(self):
        return f"{[self.subject_code]} {self.subject_name}\n  Units: {self.units}\n  Instructor: {self.instructor.full_name}"

    # def refresh_student_subjects(self, student):
    #     for subject in student.subjects:
    #         subject_code = subject.subject_code
    #         student.grades[subject_code] = {
    #             "Prelim": None,
    #             "Midterm": None,
    #             "Final": None,
    #             "Average": None,
    #             "Grade": None,
    #         }

    # def add_subject(self, student):
    #     if self not in student.subjects:
    #         student.subjects.append(self)
    #         # self.refresh_student_subjects(student)
    #         for subject in student.subjects:
    #             subject_code = subject.subject_code
    #             student.grades[subject_code] = {
    #                 "Prelim": None,
    #                 "Midterm": None,
    #                 "Final": None,
    #                 "Average": None,
    #                 "Grade": None,
    #             }
    #     else:
    #         print("You are already enrolled in this subject.")

    # def drop_subject(self, student):
    #     if self in student.subjects:
    #         student.subjects.remove(self)
    #         # Remove the corresponding grades entry
    #         if self.subject_code in student.grades:
    #             del student.grades[self.subject_code]
    #         print(f"You have dropped [{self.subject_code}] {self.subject_name}.")
    #     else:
    #         print("You are not enrolled in this subject.")
    # if self in student.subjects:
    #     student.subjects.remove(self)
    #     del student.grades[self.subject_code]
    #     print(f"You have dropped [{self.subject_code}] {self.subject_name}.")
    # # else:
    # #     print("You are not enrolled in this subject.")
