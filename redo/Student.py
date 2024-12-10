from User import User
from Subject import Subject


class Student(User):
    def __init__(self, first_name, last_name, student_id, program, section):
        # user_id = f"S{student_count}"
        user_id = student_id
        super().__init__(first_name, last_name, "student", user_id)
        self.__student_id = user_id
        self.program = program
        self.section = section
        self.year = section.get_year()
        self.semester = section.get_semester()
        self.grades = {}
        self.gwa = None
        self.balance = 0.00
        self.scholarship = None

        self.__subjects = []
        for subject in section.get_subjects():
            self.__subjects.append(
                Subject(
                    subject.get_subject_code(),
                    subject.get_subject_name(),
                    subject.get_units(),
                    subject.get_tuition(),
                    subject.get_instructor(),
                )
            )

            subject_code = subject.get_subject_code()
            self.grades[subject_code] = {
                "Prelim": None,
                "Midterm": None,
                "Final": None,
                "Average": None,
                "Grade": None,
            }

    def get_subjects(self):
        return self.__subjects

    def get_student_id(self):
        return self.__student_id

    def calculate_balance(self):
        if self.__subjects:
            total_tuition = 0
            for subject in self.__subjects:
                subject_tuition = subject.get_units() * subject.get_tuition()
                total_tuition += subject_tuition
            if self.scholarship:
                self.balance = self.scholarship.deduct_tuition(total_tuition)
            else:
                self.balance = total_tuition
        else:
            print("No subjects enrolled. Add subjects first.")

    def view_balance(self):
        self.calculate_balance()
        return f"Balance: ₱{self.balance}"

    def view_subjects(self):
        if self.__subjects:
            print("Subjects:")
            for subject in self.__subjects:
                print(subject.view_details())
        else:
            print("No subjects enrolled.")

    def check_grades_completed(self):
        for periods in self.grades.values():
            for grade in periods.values():
                if not grade:
                    return False
        return True

    def view_grades(self):
        if self.grades:
            grades = "Grades:"
            for subject_code, periods in self.grades.items():
                grades += f"\n  [{subject_code}]:"
                # self.grades[subject_code]["Average"] = self.calculate_subject_average(
                #     subject_code
                # )

                # is_grades_complete = True
                # for period, grade in periods.items():
                #     if not grade:
                #         is_grades_complete = False
                #     grades += f"\n    {period}: {grade}"

                for period, grade in periods.items():
                    grades += f"\n    {period}: {grade}"

                grades += "\n"
            # if self.check_grades_completed():
            grades += f"\nGeneral Weighted Average: {self.compute_gwa()}"
            # else:
            #     grades += "\nGeneral Weighted Average: None"
            return grades
        else:
            return "No subjects enrolled."

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

    def calculate_subject_averages(self):
        for subject_code in self.grades:
            if subject_code not in self.grades:
                print(f"{subject_code} not found.")
                return

            subject_grades = self.grades[subject_code]
            prelim_grade = subject_grades["Prelim"]
            midterm_grade = subject_grades["Midterm"]
            final_grade = subject_grades["Final"]

            if prelim_grade and midterm_grade and final_grade:
                average = round((prelim_grade + midterm_grade + final_grade) / 3)
                subject_grades["Average"] = average
                subject_grades["Grade"] = self.convert_grades(average)
                # return average
            else:
                subject_grades["Average"] = None
                subject_grades["Grade"] = None
                # return None

    def convert_grades(self, average):
        if average >= 98:
            return 1.00
        elif 97 <= average >= 95:
            return 1.25
        elif 94 <= average >= 92:
            return 1.50
        elif 91 <= average >= 90:
            return 1.75
        elif 89 <= average >= 88:
            return 2.00
        elif 87 <= average >= 85:
            return 2.25
        elif 84 <= average >= 82:
            return 2.50
        elif 81 <= average >= 80:
            return 2.75
        elif 79 <= average >= 75:
            return 3.00
        else:
            return 5.00

    def compute_gwa(self):
        if self.check_grades_completed():
            gwa = 0
            for periods in self.grades.values():
                gwa += periods["Grade"]
            self.gwa = round(gwa / len(self.grades), 2)
            return self.gwa
        else:
            return None

    def has_grade(self, subject_code, period):
        if not self.grades[subject_code][period]:
            return False
        return True

        # return self.grades[subject_code][period] is not None
        # return grade

    def add_grade(self, subject_code, period, grade):
        self.grades[subject_code][period] = grade

    def scholarship_process(self, portal):
        self.calculate_subject_averages()
        self.compute_gwa()
        if self.gwa:
            eligible_scholarships = []
            for scholarship in portal.get_scholarships():
                if scholarship.verify_eligibility(self.gwa):
                    eligible_scholarships.append(scholarship)

            if eligible_scholarships:
                best_scholarship = eligible_scholarships[0]

                for scholarship in eligible_scholarships:
                    if scholarship.get_discount() > best_scholarship.get_discount():
                        best_scholarship = scholarship
                print(
                    f"You are eligible for {best_scholarship.get_discount() * 100}% Discount {best_scholarship.get_type()} Scholarship"
                )
                while True:
                    confirm = input("Would you like to apply for it? [Y/n]: ").lower()

                    if confirm == "n":
                        break
                    elif confirm == "y" or confirm == "":
                        best_scholarship.apply(self)
                        print(self.view_balance())
                        break
                    else:
                        print("Invalid option.")
            else:
                print("Sorry. You are not eligible for any scholarships.")

        else:
            print("Grades not yet completed.")

    def dashboard(self, portal):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Subjects")
            print("[2] View Grades")
            print("[3] View Balance")
            print("[4] Profile")
            print("[5] Apply for Scholarship")
            # print("[6] Add Subject")
            # print("[7] Drop Subject")
            print("[6] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 2, 3, 4, 5, 6, 0]: ")
            print()

            if menu_option == "1":
                self.view_subjects()

            elif menu_option == "2":
                self.calculate_subject_averages()
                print(self.view_grades())

            elif menu_option == "3":
                print(self.view_balance())

            elif menu_option == "4":
                self._profile.setupProfile()
                self._profile.viewProfile()
                while True:
                    choice = input(
                        "\n\t(0) Go Back to Dashboard\n\t(1) Update Profile\n\n> "
                    )
                    if choice == "0":
                        break
                    elif choice == "1":
                        self._profile.updateProfile()
                        break
                    else:
                        print("\nInvalid option.\n")

            elif menu_option == "5":
                self.scholarship_process(portal)

            # elif menu_option == "6":
            #     self.scholarship_process(portal)

            # elif menu_option == "7":
            #     print(self.view_subjects())
            #     subject_input = input("Enter subject code to drop: ").upper()

            #     subject_to_drop = None
            #     for subject in self.__subjects:
            #         if subject.subject_code == subject_input:
            #             subject_to_drop = subject
            #             break
            #     if subject_to_drop:
            #         subject.drop_subject(self)
            #     else:
            #         print("Subject not found.")

            elif menu_option == "6":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                break

            else:
                print("Invalid option, please try again.")
