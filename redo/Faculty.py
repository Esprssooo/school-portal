from User import User


class Faculty(User):
    def __init__(self, first_name, last_name, faculty_id):
        # user_id = f"F{faculty_count}"
        user_id = faculty_id
        super().__init__(first_name, last_name, "faculty", user_id)
        self.faculty_id = user_id
        self.classes = {}

    def view_classes(self):
        if not self.classes:
            classes = "No classes assigned."
        else:
            classes = "Your classes: "
            for subject, sections in self.classes.items():
                classes += f"\n  {subject}: "
                for section in sections:
                    classes += f"\n  - {section.section_name} "
        return classes

    def input_grade(self, period, section):
        assigned_subject = None
        for subject in section.subjects:
            if subject.subject_name in self.classes:
                print(subject)
                assigned_subject = subject

        if assigned_subject:
            print(f"Grading students in {section.section_name} for {period}: ")
            for student in section.students:
                # skip students with grade
                if student.has_grade(assigned_subject, period):
                    continue

                while True:
                    grade = float(
                        input(
                            f"Enter grade for {student.last_name}, {student.first_name}: "
                        )
                    )
                    if grade and 0.00 <= grade <= 100:
                        student.add_grade(assigned_subject, period, grade)
                        break
                    else:
                        print("Invalid grade input.")
        else:
            print(
                f"You are not assigned to any subject in section {section.section_name}."
            )

    def grade_section(self, section_name):
        section_found = None
        for sections in self.classes.values():
            for section in sections:
                if section.section_name == section_name:
                    section_found = section
                    while True:
                        print(section_found)
                        print("[1] Prelim")
                        print("[2] Midterm")
                        print("[3] Final")
                        period = input("Choose period to grade [1, 2, 3]: ")

                        if period == "1":
                            self.input_grade("Prelim", section_found)
                            break
                        elif period == "2":
                            self.input_grade("Midterm", section_found)
                            break
                        elif period == "3":
                            self.input_grade("Final", section_found)
                            break
                        else:
                            print("Invalid option.")
                    break
        if not section_found:
            print("Section not found.")

    def dashboard(self):
        while True:
            print("\n-------- SPCF Portal --------")
            print("[1] View Classes")
            print("[2] Grade Students")
            print("[4] Change Password")
            print("[0] Logout")
            menu_option = input("Choose a menu option [1, 2, 0]: ")
            print()

            if menu_option == "1":
                print(self.view_classes())

            elif menu_option == "2":
                print(self.view_classes())
                section = input("\nChoose section to grade: ").upper()
                self.grade_section(section)

            elif menu_option == "4":
                self.change_password()

            elif menu_option == "0":
                self.logout()
                faculty = None
                break

            else:
                print("Invalid option, please try again.")
