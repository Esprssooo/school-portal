class Subject:
    def __init__(self, subject_code, subject_name, units, tuition_per_unit, instructor):
        self.__subject_code = subject_code
        self.__subject_name = subject_name
        self.__units = units
        self.__tuition_per_unit = tuition_per_unit
        self.__instructor = instructor

    def get_subject_code(self):
        return self.__subject_code

    def get_subject_name(self):
        return self.__subject_name

    def get_units(self):
        return self.__units

    def get_tuition(self):
        return self.__tuition_per_unit

    def get_instructor(self):
        return self.__instructor

    def view_details(self):
        return f"{[self.__subject_code]} {self.__subject_name}\n  Units: {self.__units}\n  Instructor: {self.__instructor.get_full_name()}"

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
