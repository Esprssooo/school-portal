from User import User


class Student(User):
    def __init__(self, first_name, last_name, student_id, program, section):
        # user_id = f"S{student_count}"
        user_id = student_id
        super().__init__(first_name, last_name, "student", user_id)
        self.student_id = user_id
        self.program = program
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
        self.calculate_balance()
        return f"Balance: {self.balance}"

    def view_subjects(self):
        if self.subjects:
            subjects = "Subjects:"
            for subject in self.subjects:
                subjects += f"\n  [{subject.subject_code}] {subject.subject_name}\n    Units: {subject.units}\n    Instructor: {subject.instructor.full_name}"
                subjects += "\n"
            return subjects
        else:
            return f"No subjects enrolled."

    def view_grades(self):
        if self.grades:
            grades = "Grades:"
            for subject_code, periods in self.grades.items():
                grades += f"\n  [{subject_code}]:"
                for period, grade in periods.items():
                    grades += f"\n    {period}: {grade}"

                grades += "\n"
                print(self.calculate_subject_average(subject_code))
            return grades
        else:
            return f"No subjects enrolled."

        # if self.grades:
        #     grades = "Grades:"
        #     for subject_code, periods in self.grades.items():
        #         grades += f"\n  [{subject_code}]:"

        #         for period, grade in periods.items():
        #             grades += f"\n    {period}: {grade}"

        #         grades += "\n"
        #     return grades
        # else:
        #     return f"No subjects enrolled."

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

    def dashboard(self):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Subjects")
            print("[2] View Grades")
            print("[3] View Balance")
            print("[4] View Profile")
            print("[5] Edit Profile")
            print("[6] Reset Profile")
            print("[7] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 0]: ")
            print()

            if menu_option == "1":
                print(self.view_subjects())

            elif menu_option == "2":
                print(self.view_grades())

            elif menu_option == "3":
                print(self.view_balance())

            elif menu_option == "4":
                print(self.view_balance())

            elif menu_option == "5":
                print(self.view_balance())

            elif menu_option == "6":
                print(self.view_balance())

            elif menu_option == "7":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                break

            else:
                print("Invalid option, please try again.")
