from User import User


class Student(User):
    def __init__(self, first_name, last_name, student_count, section):
        user_id = f"S{student_count}"
        super().__init__(first_name, last_name, "student", user_id)
        self.student_id = user_id
        self.section = section
        self.year = section.year
        self.semester = section.semester
        self.subjects = section.subjects
        self.grades = {}
        self.balance = 0.00

        for subject in self.subjects:
            subject_code = subject.subject_code
            self.grades[subject_code] = {
                "Prelim": None,
                "Midterm": None,
                "Final": None,
                "Average": None,
                "Grade": None,
            }

    def calculate_balance(self):
        if self.subjects:
            total_tuition = 0
            for subject in self.subjects:
                subject_tuition = subject.units * subject.tuition_per_unit
                total_tuition += subject_tuition
            self.balance = total_tuition
        else:
            print("No subjects enrolled. Add subjects first.")

    def view_balance(self):
        return f"Balance: {self.balance}"

    def view_grades(self):
        grades_message = "Grades:"
        for subject_code, periods in self.grades.items():
            grades_message += f"\n  [{subject_code}]:"

            for period, grade in periods.items():
                grades_message += f"\n    {period}: {grade}"

            grades_message += "\n"
        return grades_message

    def calculate_subject_average(self, subject_code):
        if subject_code not in self.grades:
            return f"{subject_code} not found."

        subject_grades = self.grades[subject_code]
        prelim_grade = subject_grades["Prelim"]
        midterm_grade = subject_grades["Midterm"]
        final_grade = subject_grades["Final"]

        if prelim_grade and midterm_grade and final_grade:
            average = round((prelim_grade + midterm_grade + final_grade) / 3)
            subject_grades["Average"] = average
            return average
        else:
            return "Grades incomplete."
